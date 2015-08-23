from bs4 import BeautifulSoup

class Entry():

    def __init__(self, item):
        self.title= item.title.string
        #below might lead to issues depending on how tags are parsed
        temp_link = item.link.string
        self.link = temp_link if temp_link is not None else item.link['href']
