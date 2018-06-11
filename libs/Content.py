# Python libraries
import urllib2
from bs4 import NavigableString, Tag, BeautifulSoup
from selenium import webdriver

class Content(object):

    def fromUrl(self, url = None):
        # Query the website and return the html to the variable '_content'
        _remoteFile = urllib2.urlopen(url)
        _content = _remoteFile.read()
        _remoteFile.close()

        # Parse the html using beautiful soup and store in variable '_soup'
        _soup = self.createSoup(_content)
        return _soup

    def simulateBrowser(self, url = None):
        browser = webdriver.PhantomJS()
        browser.get(url)
        _content = browser.page_source

        # Parse the html using beautiful soup and store in variable '_soup'
        _soup = self.createSoup(_content)
        return _soup

    def createSoup(self, content = None):
        _soup = BeautifulSoup(content, 'html.parser')
        return _soup