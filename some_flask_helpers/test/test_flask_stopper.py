# -*- coding: utf-8 -*-

# Copyright (C) 2021  Marcus Rickert
#
# See https://github.com/marcus67/some_flask_helpers
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import os
import flask
import unittest
import time
import threading

from some_flask_helpers import flask_stopper

class TestFlaskStopper(unittest.TestCase):


    def run_server(self):

        port = int(os.getenv("WEB_SERVER_PORT", "6666"))
        self._app.run(port=port, host='localhost', threaded=True)
        print("stopped server")

    def test_flask_stopper(self):

        port = int(os.getenv("WEB_SERVER_PORT", "6666"))

        try:
            self._app = flask.Flask('some_flask_helpers')
            self._flask_stopper = flask_stopper.FlaskStopper(p_app=self._app)


            self._process = threading.Thread(target=self.run_server)
            self._process.start()

            # wait until the server has started up
            time.sleep(1)

            print("stopping server")

            self._flask_stopper.stop(host='localhost', port=port)

            time.sleep(1)
            # wait until the server has shut down


        except Exception as e:
            raise e

        finally:
            self._flask_stopper.destroy()

    def test_flask_stopper2(self):

        # Test again to make sure the clean up teardown of server works as expected!
        self.test_flask_stopper()
