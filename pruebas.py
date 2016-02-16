import parse
import httpscrap
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
import os


############################Configuracion para tpb######################
#print (soup2.prettify())
#search/the%20flash%20s01e01/0/7/0 el 7 es el parametro para ordenar por seeders.

soup2 = httpscrap.request_soup("https://thepiratebay.se/search/the%20flash%20s01e01/0/7/0")
magnet = parse.get_link(str(httpscrap.get_tag('a','title','Download this torrent using magnet',soup2)))
#magnet = httpscrap.get_tag('a','title','Download this torrent using magnet',soup2)

#print (magnet)
#magnet = "magnet:?xt=urn:btih:25f93ec791cac716bbca3844ec13747719bdaa57&amp;dn=The+Flash+2014+S01E01+720p+HDTV+X264-DIMENSION+%5Beztv%5D&amp;tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&amp;tr=udp%3A%2F%2Fopen.demonii.com%3A1337&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
os.startfile(magnet)


