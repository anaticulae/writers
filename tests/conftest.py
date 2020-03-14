# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import pytest
import utila

import tests.update
import writers.generator
import writers.web

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

if not 'PYTEST_XDIST_WORKER' in os.environ:
    if 'GENERATE' in os.environ or utila.test.LONGRUN:
        utila.log('install requirements')
        tests.update.install_requirements()

        tests.update.update_resources()

MSG = (f'could not locate: {writers.build()}\n'
       'run `baw --test=generate` to generate')
assert os.path.exists(writers.build()), MSG


@pytest.fixture
def app(testdir):
    """Create and configure a new app instance for each test."""
    root = testdir.tmpdir
    assert writers.generator.generate(path=root) == utila.SUCCESS
    application = writers.web.create(path=root)
    yield application


@pytest.fixture
def client(app):  # pylint:disable=W0621
    """A test client for the app."""
    return app.test_client()
