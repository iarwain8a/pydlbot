import parse
import httpscrap
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import re
import os

#soup = BeautifulSoup(urlopen("http://www.ambito.com/economia/mercados/monedas/dolar/"),"html.parser")
#soup = httpscrap.request_soup("http://www.ambito.com/economia/mercados/monedas/dolar/")

#venta = parse.only_numbers(httpscrap.get_tag('div','class','cierreAnterior',soup),",")
#compra = parse.only_numbers(httpscrap.get_tag('div','class', 'ultimo',soup),",")

#print ("Venta:",venta)
#print ("Compra:",compra)


############################Configuracion para tpb######################
#print (soup2.prettify())
#search/the%20flash%20s01e01/0/7/0 el 7 es el parametro para ordenar por seeders.

soup2 = httpscrap.request_soup("https://thepiratebay.se/search/the%20flash%20s01e01/0/7/0")

#print (httpscrap.get_tag('table','id','searchResult',soup2).find_all('a','href'))
#print (httpscrap.get_tag('a','title','Download this torrent using magnet',soup2))
magnet = "magnet:?xt=urn:btih:25f93ec791cac716bbca3844ec13747719bdaa57&amp;dn=The+Flash+2014+S01E01+720p+HDTV+X264-DIMENSION+%5Beztv%5D&amp;tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&amp;tr=udp%3A%2F%2Fopen.demonii.com%3A1337&amp;tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&amp;tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
os.startfile(magnet)



#links = SoupStrainer ('a',href=re.compile('magnet:?'))
#print(BeautifulSoup(soup2.text,parseOnlyThese=links))

#g = soup2.recursiveChildGenerator()
#while True:
#    try:
#        print (g.__next__())
#    except StopIteration:
#        break

#first_link = httpscrap.get_tag('div','class','detName',soup2)

#first_link = httpscrap.get_tag('a href','','',soup2)

#print (first_link)
