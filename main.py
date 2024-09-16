from PIL import Image
import imagehash

image1 = Image.open('1.jpg')
image2 = Image.open('2.jpg')

hash1=imagehash.average_hash(image1)
hash2=imagehash.average_hash(image2)
cutoff = 5


if hash1 - hash2 < cutoff:
    print("Images are similar")
else:
    print("Images are not similar")
