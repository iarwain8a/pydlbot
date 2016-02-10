from bs4 import BeautifulSoup
from urllib.request import urlopen

def request_soup(url):
    soup = BeautifulSoup(urlopen(url),"html.parser")
    return soup

def get_tag(tag,atributes,className,soup):
    return soup.body.find(tag, attrs={atributes:className}).text
