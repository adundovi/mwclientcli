import mwclientcli.libs.mwinterface

class Command(object):
    """Meta-class for every command
    """
    def __init__(self):
        self.args = []
        self.help = None
        self.name = None
        self.parser = None
        self.site = None

    def init_parser(self, subparsers):

        self.parser = subparsers.add_parser(self.name, help=self.help)

    def invoke(self):
        """Establish the connection to the wiki
           when called and run process()
        """
        self.site = mwclientcli.libs.mwinterface.MWInterface()
        self.process()

    def process(self):
        """Command-specific part
        """
        pass
