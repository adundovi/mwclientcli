# -*- coding: utf-8 -*-

import sys
import mwclient

from mwclientcli.libs.config import Settings

class MWInterface(object):
    
    def __init__(self):

        s = Settings()
        if s.get('path'):
            self.site = mwclient.Site(s.get('url'), path=s.get('path'))
        else:
            self.site = mwclient.Site(s.get('url'))
        self.site.login(s.get('username'), s.get('password'))

    def output(self, string):
        sys.stdout.write(string.encode('utf-8') + '\n')

    def print_all_namespaces(self):

        for key, value in self.site.namespaces.iteritems():
            self.output(str(key)+' => '+value)

    def print_all_categories(self, namespace=0):

        for i in self.site.allcategories():
            self.output(i.name)

    def print_all_pages(self, namespace=0):
       
        for i in self.site.allpages(namespace=namespace):
            self.output(i.name)

    def print_all_users(self):

        for i in self.site.allusers():
            self.output(i['name'])

    def get_page(self, page_title='Main_Page'):
        
        page = self.site.Pages[page_title]
        self.output('{scheme}://{host}/wiki/{title}'.format(scheme='https',
                                                            host=self.site.host,
                                                            title=page_title))
        return page.text()

    def move(self, page_title, new_title):

        page = self.site.Pages[page_title]
        page.move(new_title)

    #def parse( self, page_title ):
    #
    #    page = self.site.parse( page=page_title )
    #
    #    parser = LaTeXBuilder()
    #    parser.doc( page['text']['*'] )
    #    parser.output()

    def set_page(self, page_title, content, summary=''):
        if page_title == '':
            return
        page = self.site.Pages[page_title]
        page.save(content, summary=summary)

    def print_page(self, page_title='Main_Page'):
        self.output(self.get_page(page_title))

    def search(self, query, namespace='0'):

        for result in self.site.search(query, namespace=namespace, what='text'):
            self.output(result['title'])
            #self.output(result['snippet'])

