from PIL import Image
from pprint import pprint

print("Opening Image...")
## Opens Image
im = Image.open('image.png')
pix = im.load()
size = im.size

result = []
row = []

## Iterates through each x and y coordinate
print("Getting RGBA Data...")
for x in range(0, 512):
    row = []
    for y in range(-512, 0):
        r = pix[x, y][0]
        g = pix[x, y][1]
        b = pix[x, y][2]
        added_num = r + g + b
        row.append(round(added_num / 3, 2))
    result.append(row)

print("Writing to results.txt...")
with open("results.txt", "w+") as f:
    f.write(str(result))