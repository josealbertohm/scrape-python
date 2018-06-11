import json

class Character(object):
    def __init__(self):
        self._name  = None
        self._title = None
        self._url   = None
        self._img   = None

    @property 
    def name(self):
        return self._name 
    @name.setter
    def name(self, value):
        self._name = value 

    @property 
    def title(self):
        return self._title 
    @title.setter
    def title(self, value):
        self._title = value 

    @property 
    def img(self):
        return self._img 
    @img.setter
    def img(self, value):
        self._img = value 

    @property 
    def url(self):
        return self._url 
    @url.setter
    def url(self, value):
        self._url = value 

    def toJSON(self):
        return json.dumps(self.__dict__)    