from mwclientcli.libs.command import Command

class Move(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'move'
        self.help = 'Move/rename the page'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('oldtitle', nargs='?', help='Current title of the page')
        self.parser.add_argument('newtitle', nargs='?', help='New title of the page')

    def process(self):
        self.site.move(self.args.oldtitle, self.args.newtitle)
