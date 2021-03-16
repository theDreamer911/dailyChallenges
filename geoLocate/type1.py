import geocoder

ipaddress = geocoder.ip('me')
print(ipaddress.latlng)
