import os
import subprocess
import sys
import tempfile

from mwclientcli.libs.command import Command

EDITOR = os.environ.get('EDITOR', 'vim')

class Edit(Command):

    def __init__(self):
        Command.__init__(self)

        self.name = 'edit'
        self.help = 'Edit the page'

    def init_parser(self, subparsers):
        Command.init_parser(self, subparsers)

        self.parser.add_argument('title',
                                 nargs='?',
                                 default='Main_Page',
                                 help='Title of the page')

    def process(self):

        if sys.stdin.isatty():
            # when there is no piped stream
            initial_content = self.site.get_page(self.args.title).encode('utf8')
            self._runeditor(initial_content)
            return

        # handle piped stream
        buffer = []
        for line in sys.stdin:
            buffer.append(line)
        initial_content = "".join(buffer)
        self.site.set_page(self.args.title, initial_content)

    def _runeditor(self, initial_content):

        with tempfile.NamedTemporaryFile(suffix=".tmp") as temp:

            temp.write(initial_content)
            temp.flush()
            subprocess.call([EDITOR, temp.name], stdin=None)
            temp.seek(0)
            new_content = temp.read()

            if new_content == initial_content:
                print "Nothing new."
            else:
                self.site.set_page(self.args.title, new_content)
                print "Page saved"
