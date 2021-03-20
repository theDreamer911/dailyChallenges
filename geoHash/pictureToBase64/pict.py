import base64
with open('apple.jpg', 'rb') as img_file:
    strings = base64.b16encode(img_file.read())
print(strings.decode('utf-8'))
