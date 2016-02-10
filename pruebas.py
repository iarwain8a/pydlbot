import parse
import httpscrap
from bs4 import BeautifulSoup
from urllib.request import urlopen

#soup = BeautifulSoup(urlopen("http://www.ambito.com/economia/mercados/monedas/dolar/"),"html.parser")
soup = httpscrap.request_soup("http://www.ambito.com/economia/mercados/monedas/dolar/")

venta = parse.only_numbers(httpscrap.get_tag('div','class','cierreAnterior',soup),",")
compra = parse.only_numbers(httpscrap.get_tag('div','class', 'ultimo',soup),",")

print ("Venta:",venta)
print ("Compra:",compra)
