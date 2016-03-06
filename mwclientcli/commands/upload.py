from mwclientcli.libs.command import Command

class Upload(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'upload'
        self.help = 'Upload a file'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('file', nargs='?', help='Path to the local file')
        self.parser.add_argument('description', nargs='?', help='File description')

    def process(self):
        self.site.upload(self.args.file, self.args.description)
