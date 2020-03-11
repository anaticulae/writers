# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila
import utila.cli

import writers
import writers.generator
import writers.web


@utila.saveme
def main():
    commands = [
        utila.cli.Flag('--generate', message=('generate documents')),
        utila.cli.Flag('--run', message=('run webserver')),
    ]
    parser = utila.cli.create_parser(
        todo=commands,
        config=utila.ParserConfiguration(
            outputparameter=False,
            inputparameter=False,
            prefix=False,
        ),
        version=writers.__version__,
    )
    args = utila.parse(parser)
    if args['generate'] or args['run']:
        if writers.generator.generate():
            return utila.FAILURE
    if args['run']:
        if writers.web.run():
            return utila.FAILURE

    return utila.SUCCESS
