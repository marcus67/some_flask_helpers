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

import threading
import time
import unittest
import os

import flask
import requests

from some_flask_helpers import blueprint_adapter
from some_flask_helpers import flask_stopper
from some_flask_helpers import test

MY_BLUEPRINT_NAME = "MyBlueprintName"
MY_BLUEPRINT_ADAPTER = blueprint_adapter.BlueprintAdapter()


class SomeMethodHandler(object):

    def __init__(self, p_app):
        self._app = p_app
        self.status = False

        # Install the handler
        self._blueprint = flask.Blueprint(MY_BLUEPRINT_NAME, test.__name__)
        MY_BLUEPRINT_ADAPTER.assign_view_handler_instance(p_blueprint=self._blueprint, p_view_handler_instance=self)
        MY_BLUEPRINT_ADAPTER.check_view_methods()
        self._app.register_blueprint(self._blueprint)

    @classmethod
    def destroy(cls):
        MY_BLUEPRINT_ADAPTER.unassign_view_handler_instances()

    @MY_BLUEPRINT_ADAPTER.route_method(p_rule="/api/set_status_true")
    def some_handler_method(self):
        self.status = True
        return flask.Response("OK", mimetype='application/txt')


class TestBluePrintAdapter(unittest.TestCase):

    def run_server(self):

        port = int(os.getenv("WEB_SERVER_PORT", "6666"))
        self._app.run(port=port, host='localhost', threaded=True)
        print("stopped server")

    def test_blue_print_adapter(self):

        port = int(os.getenv("WEB_SERVER_PORT", "6666"))

        try:
            self._app = flask.Flask('some_flask_helpers')
            self._flask_stopper = flask_stopper.FlaskStopper(p_app=self._app)

            self._my_handler = SomeMethodHandler(p_app=self._app)

            self._process = threading.Thread(target=self.run_server)
            self._process.start()

            self.assertFalse(self._my_handler.status)

            # wait until the server has started
            time.sleep(1)

            url = "http://localhost:{port}/api/set_status_true"
            r = requests.get(url.format(port=port))

            self.assertEqual(r.status_code, 200)
            self.assertIsNotNone(r.text)
            self.assertEqual(r.text, "OK")
            self.assertTrue(self._my_handler.status)

            print("stopping server")

            self._flask_stopper.stop(host='localhost', port=port)

            # wait until the server has shut down (before the test has officially terminated)
            time.sleep(1)

        except Exception as e:
            raise e

        finally:
            self._flask_stopper.destroy()
            self._my_handler.destroy()
