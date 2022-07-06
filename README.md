# some_flask_helpers

This is a little Simple Extensions to the Flask Framework:

*   The class `BlueprintAdapter` allows you to use blueprints as decorators.

*   The class `FlaskStopper` defines a Flask blueprint to add a clean shut-down mechanism to a Flask web server which 
    may come in handy for test cases which have to start and tear down Flask servers repeatedly.

## Source Repository ##

See https://github.com/marcus67/some_flask_helpers

## CircleCI Continuous Integration Status

<A HREF="https://circleci.com/gh/marcus67/some_flask_helpers/tree/master"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/some_flask_helpers.svg?label=Python3%20master"></A> 

## GitHub Status

<A HREF="https://github.com/marcus67/some_flask_helpers"><IMG SRC="https://img.shields.io/github/forks/marcus67/some_flask_helpers.svg?label=forks"></A> <A HREF="https://github.com/marcus67/some_flask_helpers/stargazers"><IMG SRC="https://img.shields.io/github/stars/marcus67/some_flask_helpers.svg?label=stars"></A> <A HREF="https://github.com/marcus67/some_flask_helpers/watchers"><IMG SRC="https://img.shields.io/github/watchers/marcus67/some_flask_helpers.svg?label=watchers"></A> <A HREF="https://github.com/marcus67/some_flask_helpers/issues"><IMG SRC="https://img.shields.io/github/issues/marcus67/some_flask_helpers.svg"></A> <A HREF="https://github.com/marcus67/some_flask_helpers/pulls"><IMG SRC="https://img.shields.io/github/issues-pr/marcus67/some_flask_helpers.svg"></A>

## Versions

### Version 0.2.3 (July 5th 2022)

* Terminate flask server by monkey patching `werkzeug.serving.make_server` instead of using 
  request environment setting `werkzeug.server.shutdown`

### Version 0.2.2 (February 14th 2021)

*   Include required files in MANIFEST.in

### Version 0.2.1 (February 14th 2021)

*   Activate Markdown for project description on PyPi

### Version 0.2 (February 14th 2021)

*   Add test cases

### Version 0.1

*   Initial version

## Usage Examples ##

See the testcase for usage examples:

*    [`BluePrintAdapter`](some_flask_helpers/test/test_blueprint_adapter.py)  
*    [`FlaskStopper`](some_flask_helpers/test/test_flask_stopper.py)  
