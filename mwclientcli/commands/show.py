from mwclientcli.libs.command import Command

class Show(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'show'
        self.help = 'Show the page'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('title',
                                 nargs='?',
                                 default='Main_Page',
                                 help='Title of the page')

    def process(self):
        self.site.print_page(self.args.title)
