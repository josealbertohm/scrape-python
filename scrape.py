# Python libraries
from bs4 import Tag
import os
from os.path import join, dirname
from dotenv import load_dotenv
 
from models.Character import Character
from libs.Content import Content
from libs.MySQL import MySQL

def handleGalleryItem(element):
    _data = Character()
    # Character's name
    _data.url = element.get('href').encode("utf-8") 
    # Character's title
    _data.title = element.get('title').encode("utf-8")

    # Process the div tags inside anchor tag
    for child_l1 in element:
        if type(child_l1) is Tag and child_l1.name == 'div':
            # div tag with the Character's image
            if hasClass('category-gallery-item-image', child_l1.get('class', [])):
                for child_l2 in child_l1:
                    if type(child_l2) is Tag and child_l2.name == 'img':
                        _data.img = child_l2.get('src').encode("utf-8") 
            # div tag with the Character's full name
            elif hasClass('title', child_l1.get('class', [])):
                _data.name = child_l1.text.encode("utf-8")
    # Return the data parsed in JSON format
    return _data 

def hasClass(name, classes):
    for _name in classes:
        if name == _name: return True
    return False


def readNarutoData():
    # Web site url
    NARUTO_DATA_URL = 'http://naruto.wikia.com/wiki/Category:Characters'

    # Get HTML Content from URL
    _soup = Content().fromUrl(NARUTO_DATA_URL)

    # Take out the <div> of name and get its <div> childs
    _divGalleryRoom = _soup.find('div', attrs={'class': 'category-gallery-room1'})

    # Variable for storing all the results
    _result = {}
    # Process all the div childs (class: 'category-gallery-item')
    for _divGalleryItem in _divGalleryRoom:
        for child in _divGalleryItem:
            if type(child) is Tag:
                _item = handleGalleryItem(child)
                _result[_item.title] = _item
    
    values = []
    for _key in _result:
        print _key
        # readCharacterData(_result[_key].url)
        values.append((_result[_key].title, _result[_key].name, _result[_key].img, _result[_key].url))
    
    # Insert many records
    sql = "INSERT INTO characters_tbl (title, full_name, image, url) VALUES (%s, %s, %s, %s)"

    mysql = MySQL()
    mysql.host   = os.getenv("DB_HOST")
    mysql.user   = os.getenv("DB_USER")
    mysql.passwd = os.getenv("DB_PASS")
    mysql.dbname = os.getenv("DB_NAME")
    mysql.connect()
    mysql.update("DELETE FROM characters_tbl")
    mysql.insertMany(sql, values)
    mysql.close()

def readCharacterData(url = None):
    print("Processing url " + url)
    # Get HTML Content from URL
    _soup = Content().simulateBrowser(url)

    # Take out the <table> of name and get its row childs with the character details
    #_tableInfobox = _soup.find('table', attrs={'class': 'infobox'})
    _tableInfobox = _soup.findAll('table')

    counter = 0
    for table in _tableInfobox:
        if type(table) is Tag:
            if hasClass('infobox', table.get('class', [])):
                print table

def loadSettings():
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

if __name__ == "__main__":
    loadSettings()
    readNarutoData()
