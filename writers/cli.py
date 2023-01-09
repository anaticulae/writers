# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
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
    parser = create_parser()
    args = utila.parse(parser)
    verbose = args['verbose'] is not None
    if args['build'] or args['run']:
        if writers.generator.generate(
                dirty=args['dirty'],
                verbose=verbose,
        ):
            return utila.FAILURE
    if args['run']:
        if writers.web.run():
            return utila.FAILURE
    if args['show']:
        if writers.generator.open_generated():
            return utila.FAILURE
    return utila.SUCCESS


CMDS = [
    utila.cli.Flag('--build', message=('generate docs')),
    utila.cli.Flag('--show', message=('open generated docs')),
    utila.cli.Flag('--run', message=('run webserver')),
    utila.cli.Flag('--dirty', message=('ignore errors')),
]


def create_parser():
    parser = utila.cli.create_parser(
        todo=CMDS,
        config=utila.ParserConfiguration(
            cacheflag=False,
            inputparameter=False,
            multiprocessed=False,
            outputparameter=False,
            pages=False,
            prefix=False,
            verboseflag=True,
            waitingflag=False,
        ),
        version=writers.__version__,
    )
    return parser
