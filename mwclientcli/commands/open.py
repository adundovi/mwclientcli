from mwclientcli.libs.command import Command

import webbrowser

class Open(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'open'
        self.help = 'Open the page in the browser'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('title',
                                 nargs='?',
                                 default='Main_Page',
                                 help='Title of the page')

    def process(self):
        url = self.site.get_url(self.args.title)
        webbrowser.open(url)
