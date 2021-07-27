from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request("{change with the link you want check the url}")
pages = urlopen(req)

soup = BeautifulSoup(pages, 'lxml')
links = []

for link in soup.findAll('a'):
    links.append(link.get('href'))

print(links)
