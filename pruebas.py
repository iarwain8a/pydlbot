import parse
import httpscrap
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
import os


############################Configuracion para tpb######################
#print (soup2.prettify())
#search/the%20flash%20s01e01/0/7/0 el 7 es el parametro para ordenar por seeders.

soup2 = httpscrap.request_soup("https://thepiratebay.se/search/the%20flash%20s02e01/0/7/0")
magnet = parse.get_magnet_link(str(httpscrap.get_tag('a','title','Download this torrent using magnet',soup2)))
#magnet = httpscrap.get_tag('a','title','Download this torrent using magnet',soup2)

os.startfile(magnet)



