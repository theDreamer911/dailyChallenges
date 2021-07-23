import urllib.request
import re

with open("vallhala.txt") as f:
    text = f.read()
    urls = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

# print(urls)

for x in urls:
    print(urllib.request.urlopen(x).getcode())
