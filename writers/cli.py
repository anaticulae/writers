# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo
import utilo.cli

import writers
import writers.generator
import writers.web


@utilo.saveme
def main():
    parser = create_parser()
    args = utilo.parse(parser)
    verbose = args['verbose'] is not None
    if args['build'] or args['run']:
        if writers.generator.generate(
                dirty=args['dirty'],
                verbose=verbose,
        ):
            return utilo.FAILURE
    if args['run']:
        if writers.web.run():
            return utilo.FAILURE
    if args['show']:
        if writers.generator.open_generated():
            return utilo.FAILURE
    return utilo.SUCCESS


CMDS = [
    utilo.cli.Flag('--build', message=('generate docs')),
    utilo.cli.Flag('--show', message=('open generated docs')),
    utilo.cli.Flag('--run', message=('run webserver')),
    utilo.cli.Flag('--dirty', message=('ignore errors')),
]


def create_parser():
    parser = utilo.cli.create_parser(
        todo=CMDS,
        config=utilo.ParserConfiguration(
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
