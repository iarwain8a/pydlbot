from bs4 import BeautifulSoup
from urllib.request import urlopen

class BeautifulScrap:
	def __init__(self,url):
		self.soup = BeautifulSoup(urlopen(url),"html.parser")

	def request_soup(self):
	    return self.soup

	def get_tag(self,tag,atributes,className):
	    return self.soup.body.find(tag, attrs={atributes:className})
