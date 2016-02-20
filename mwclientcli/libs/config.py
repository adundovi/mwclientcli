from os.path import expanduser, join

import ConfigParser

class Settings(object):

    def __init__(self, config_path=None):

        self.section = 'default'
        self.config = ConfigParser.ConfigParser()

        if not config_path:
            home = expanduser('~')
            filename = '.mwclientcli.conf'
            self.config_path = join(home, filename)
        else:
            self.config_path = config_path

        self.config.read(self.config_path)

    def get(self, key, section=None):

        if not section:
            section = self.section

        try:
            return self.config.get(section, key)
        except ConfigParser.NoOptionError:
            return False

    def set(self, key, value):

        self.config.set(self.section, key, value)
