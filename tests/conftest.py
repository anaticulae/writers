# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import pytest
import utila

import writers.generator
import writers.web

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    if os.path.exists(writers.html()):
        return
    build = writers.build()
    os.makedirs(build, exist_ok=True)
    returncode = writers.generator.generate(path=build)
    assert returncode == utila.SUCCESS


MSG = (f'could not locate: {writers.build()}\n'
       'run `baw test skip --generate` to generate')


@pytest.fixture
def app(testdir):
    """Create and configure a new app instance for each test."""
    assert os.path.exists(writers.build()), MSG
    root = testdir.tmpdir
    assert writers.generator.generate(path=root) == utila.SUCCESS
    application = writers.web.create(path=root)
    yield application


@pytest.fixture
def client(app):  # pylint:disable=W0621
    """A test client for the app."""
    return app.test_client()
