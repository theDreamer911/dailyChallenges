from PIL import Image, ImageDraw
img = Image.new('RGB', (90, 60), color='white')
# img.save('blank_image.png')

draw = ImageDraw.Draw(img)
draw.text((20, 20), "Hand", fill=(38, 38, 38))
draw.line((40, 30, 150, 300), fill=120, width=1)
draw.line((20, 30, 30, 20), fill=88, width=2)

draw.point(((30, 40), (10, 20), (14, 25), (35, 10),
            (14, 28), (17, 25)), fill="black")

img.save('blank_image4.png')
