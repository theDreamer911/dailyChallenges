from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request

req = Request("{change with the link you want check the url}")
pages = urlopen(req)

soup = BeautifulSoup(pages, 'lxml')
links = []

print("Grabbing all links ...")

for link in soup.findAll('a'):
    links.append(link.get('href'))

print("Checking links...\n")

for x in links:
    try:
        print(x + ": " + urllib.request.urlopen(x).getcode())
    except:
        print('link error')
