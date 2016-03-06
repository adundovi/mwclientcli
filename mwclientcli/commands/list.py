from mwclientcli.libs.command import Command

class List(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'list'
        self.help = 'List pages/categories/namespaces...'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('item', nargs='?',
                                 default='pages',
                                 choices=['pages', 'categories', 'namespaces',
                                          'users', 'files'],
                                 help='List specified class of objects')
        self.parser.add_argument('-n', '--namespace',
                                 default='0',
                                 help='Include following namespace(s)\n \
                                 Use | to separate multiple namespace')


    def process(self):

        if self.args.item == 'categories':
            self.site.print_all_categories(namespace=self.args.namespace)

        if self.args.item == 'pages':
            self.site.print_all_pages(namespace=self.args.namespace)

        if self.args.item == 'namespaces':
            self.site.print_all_namespaces()

        if self.args.item == 'users':
            self.site.print_all_users()

        if self.args.item == 'files':
            self.site.list_files()
