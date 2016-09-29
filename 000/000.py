from PIL import Image

base = Image.open('base.png')
number = Image.open('number.png')

area = (0, 0, 25, 33)
result = base.paste(number, area)
base.show()
