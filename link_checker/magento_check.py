import urllib.request

f = open('magento.txt', 'r')

f.read()

f.close()
# urls = []

# [urls.extend(url) for url in f.readline()]

# print(urls)

# for x in f:
# print(x.readline())

# print(f.read())

# full = open('active.txt', 'a')
# for x in f.read():
#     try:
#         print(x + " : " + urllib.request.urlopen(x).getcode())
#     except:
#         pass
# # full.close()

# print(urllib.request.urlopen('http://murahtenan.com').getcode())
