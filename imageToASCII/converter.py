# Import the modules
# import sys
from PIL import Image

# Get your Image Information
pict = Image.open('arya_stark.jpg')
height, width = pict.size
# print(width, height)

# print(f'height: {height}px and width: {width}px')
aspect_ratio = height/width
# print(aspect_ratio)

# Convert the Image into ASCII
new_width = 240
new_height = aspect_ratio * new_width*0.5
pict = pict.resize((new_width, int(new_height)))
pict = pict.convert('L')
pixels = pict.getdata()
chars = ["i", "o", "#", "%", "!", "-", ":", ":", "&", "*", "i"]
new_pixels = [chars[pixel//25] for pixel in pixels]
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_picture = [new_pixels[index:index+new_width]
                 for index in range(0, new_pixels_count, new_width)]
ascii_picture = "\n".join(ascii_picture)

# image_path = sys.argv[0]
with open('ascii_picture.txt', 'w') as file:
    file.write(ascii_picture)
