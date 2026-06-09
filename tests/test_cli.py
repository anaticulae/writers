# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import webbrowser

import utilotest

import tests


def test_cli_help(mp):
    tests.run_writers('--help', mp=mp)


@utilotest.longrun
def test_cli_build(td, mp):  # pylint:disable=W0613
    tests.run_writers('--build', mp=mp)


@utilotest.longrun
def test_cli_show(td, mp):  # pylint:disable=W0613
    with mp.context() as context:
        context.setattr(webbrowser, 'open', lambda x: x)
        tests.run_writers('--show', mp=mp)
