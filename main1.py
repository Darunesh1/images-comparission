from PIL import Image,ImageChops

img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")

# image chanels operations containd calucation methods for images

diff=ImageChops.difference(img1,img2)

if diff.getbbox():
    diff.show()
