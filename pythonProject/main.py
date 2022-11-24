from PIL import Image
import os

def filenametofind():
    pathToTheFile = input("Write file name: ")
    return pathToTheFile

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


def phototoasci(img_path):
    rotated = Image.open(img_path).convert('RGB')
    im = rotated.rotate(90)
    heighOfTheFile = im.height
    widthOfTheFile = im.width
    with open('result.txt', 'w') as f:
        for i in range(0, heighOfTheFile):
            for j in range(0, widthOfTheFile):
                r, g , b = im.getpixel((i, j))
                print(r)
                if(r>200):
                    f.write(str(chr(122)))
                elif (r > 150):
                    f.write(str(chr(43)))
                elif (r > 100):
                    f.write(str(chr(45)))
                elif (r > 50):
                    f.write(str(chr(61)))
                elif (r <= 50):
                    f.write(str(chr(23)))

            f.write("\n")

phototoasci(findfile(filenametofind(), "photos\\"))
