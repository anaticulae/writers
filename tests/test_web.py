# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import tests


def test_web_run(client):
    result = tests.content(client, '/')
    assert len(result) > 300, str(result)
    assert 'Schreibhilfe' in result


def test_web_run_page_not_found(client):
    result = tests.content(client, '/this_page_is_not_there')
    assert len(result) > 300, str(result)
    assert 'Schreibhilfe' in result
