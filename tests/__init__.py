#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2020-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import http

import utilatest

import writers
import writers.cli


def run_writers(cmd: str, monkeypatch) -> int:
    returncode = utilatest.run_command(
        cmd,
        writers.PROCESS,
        writers.cli.main,
        success=True,
        monkeypatch=monkeypatch,
    )
    return returncode


def content(client, request: str):
    response = client.get(request)
    assert response.status_code == http.HTTPStatus.OK
    # read binary data from response and convert them to str
    return response.data.decode('utf8')
