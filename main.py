'''
Workflow:
Open the Image
Read the contents (dont mess with the headers and important INFOS!)
- Extra: discover the extension of the file
Save the bytearray into a variable and modify (AGAIN, DONT MESS WITH THE HEADERS)
(How i will make the random payload to the bytearray of the image?
1 - Generate random stuff and translate to byte and insert to the bytearray
2 - ask how many interations it will make)
Write the modifications to the file and save
????
PROFIT

Research:
Type of compression in the images. The type that i am working now is JPEG;
Useful links:
https://github.com/Kareeeeem/jpglitch/blob/master/jpglitch.py
https://github.com/snorpey/glitch-canvas/
https://pillow.readthedocs.io/en/latest/
and wikipedia articles
'''

# library importing
# Only using this library for now, maybe i will need to use more? IDK

from PIL import Image
import random

# If someday i import this file to another scripts
if __name__ == "__main__":
    image = Image.open('spooky.jpeg')
    print('Is seems your are opening {} image format.'.format(image.format))
    while x <= random_size:
        random_list.append(random.sample(range(0, 100), random_size))
        x = x + 1
    # Open and transforms the image into bytearray
    with open('spooky.jpeg', 'rb') as imageFile:
        f = imageFile.read()
        bytearray_image = bytearray(f)

    print(random_list)
