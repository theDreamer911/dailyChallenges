import requests

url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = {
    'apikey': '9561c10ac3b6a8f9f99634a1246f74b9fce12d4a91ee55d3ee003101ec8d7cb6'}

# myfile = input('Masukkan nama file beserta ekstensinya: ')
files = {'file': ('Lab01-01.exe', open('Lab01-01.exe', 'rb'))}
response = requests.post(url, files=files, params=params)

urls = 'https://www.virustotal.com/gui/file'
responses = requests.post(urls, files=files, params=details)
print(responses)
