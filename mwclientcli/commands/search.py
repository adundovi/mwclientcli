from mwclientcli.libs.command import Command

class Search(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'search'
        self.help = 'Perform a full text search'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('query',
                                 nargs='?',
                                 help='Search for the query')
        self.parser.add_argument('-n', '--namespace',
                                 default='0',
                                 help='Search inside following namespace(s)\n \
                                 Use | to separate multiple namespace')

    def process(self):
        self.site.search(self.args.query, namespace=self.args.namespace)
