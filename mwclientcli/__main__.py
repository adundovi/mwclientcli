#!/usr/bin/python
# The mwclientcli executable script.

import argparse
import mwclientcli.commands

def main(args=None):
    """Regular entry point
    """
    parser = argparse.ArgumentParser(
        description='Interact with a MediaWiki site.')
    subparsers = parser.add_subparsers(title='commands',
                                       help='Choose between different commands',
                                       dest='command')

    modules = {}
    for command in mwclientcli.commands.__all__:
        inst = getattr(mwclientcli.commands, command)()
        inst.init_parser(subparsers)
        modules[command] = inst

    args = parser.parse_args()

    if args.command:
        com = modules[args.command.title()]
        com.args = args
        com.invoke()

if __name__ == "__main__":
    main()
