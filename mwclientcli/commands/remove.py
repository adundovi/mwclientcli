from mwclientcli.libs.command import Command

class Remove(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'remove'
        self.help = 'Erase the page'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('title', nargs='?', help='Title of the page')

    def process(self):
        self.site.remove(self.args.title)
