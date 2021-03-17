# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import webbrowser

import utilatest

import tests


def test_cli_help(monkeypatch):
    tests.run_writers('--help', monkeypatch=monkeypatch)


@utilatest.skip_longrun
def test_cli_build(testdir, monkeypatch):
    tests.run_writers('--build', monkeypatch=monkeypatch)


@utilatest.skip_longrun
def test_cli_show(testdir, monkeypatch):
    with monkeypatch.context() as context:
        context.setattr(webbrowser, 'open', lambda x: x)
        tests.run_writers('--show', monkeypatch=monkeypatch)
