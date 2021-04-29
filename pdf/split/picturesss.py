# from pdf2image import convert_from_path

# pages = convert_from_path('Page_0.pdf', 500, single_file=True)

# pages[0].save('out.png', 'PNG')

from pdf2image import convert_from_path
images = convert_from_path('an.pdf', 50)
for image in images:
    image.save('output.png')


images = convert_from_path('duplicate.pdf', 50)

for i, image in enumerate(images):
    image.save(f'save_{i}.png')
