from PIL import Image
import os
#Variables you should tweak to your personal interest (the code assumes the sortingReadDir is the same as croppingWriteDir
croppingReadDir = "Dataset/user_"
croppingWriteDir = "DatasetNew/user_"
sortingWriteDir = "DatasetFinal/"
GrayScale = False

#Constants, ideally you don't want to change them
CropRightExcess = (0, 0, 240, 240)
CropLeftRightExcess = (40, 0, 280, 240)
CropLeftExcess = (80, 0, 320, 240)
def Crop_Modify_Img():
    for i in range(3, 10):
        directory = croppingReadDir + str(i)
        for filename in os.listdir(directory):
            letter = str(filename)[0]
            digit = int(str(filename)[1])
            im = Image.open(directory + "/" + filename, 'r')
            if(GrayScale == True):
                im = im.convert("L")
            if i == 3:
                im = im.crop(CropRightExcess)
            elif i == 4:
                im = im.crop(CropLeftRightExcess)
            elif i == 5:
                if digit <= 4:
                    if letter < 'L':
                        im = im.crop((60, 0, 300, 240))
                    elif letter == 'L':
                        im = im.crop(CropLeftExcess)
                    else:
                        im = im.crop((60, 0, 300, 240))
                else:
                    if letter < 'L':
                        im = im.crop(CropLeftRightExcess)
                    elif letter < 'X':
                        im = im.crop((60, 0, 300, 240))
                    else:
                        im = im.crop(CropLeftExcess)

            elif i == 6:
                if digit <= 4:
                    if letter < 'H':
                        im = im.crop(CropRightExcess)
                    elif letter == 'H':
                        im = im.crop((37, 0, 277, 240))
                    elif letter == 'I' or letter == 'K':
                        im = im.crop(CropRightExcess)
                    elif letter == 'L':
                        im = im.crop(CropLeftRightExcess)
                    elif letter == 'M' or letter == 'N':
                        im = im.crop(CropRightExcess)
                    elif letter == 'O':
                        im = im.crop((14, 0, 254, 240))
                    elif letter == 'P' or letter == 'Q':
                        im = im.crop(CropRightExcess)
                    elif letter == 'R' or letter == 'S':
                        im = im.crop((14, 0, 254, 240))
                    elif letter == 'T':
                        im = im.crop((37, 0, 277, 240))
                    elif letter == 'U':
                        im = im.crop((7, 0, 247, 240))
                    elif letter == 'V':
                        im = im.crop(CropRightExcess)
                    elif letter == 'W':
                        im = im.crop((17, 0, 257, 240))
                    elif letter == 'X':
                        im = im.crop(CropRightExcess)
                    elif letter == 'Y':
                        im = im.crop((34, 0, 274, 240))
                else:
                    im = im.crop(CropLeftRightExcess)


            elif i == 7:
                if letter == 'A':
                    if digit <= 4:
                        im = im.crop((18, 0, 258, 240))
                    else:
                        im = im.crop(CropLeftRightExcess)
                elif letter == 'B':
                    if digit <= 4:
                        im = im.crop(CropRightExcess)
                    else:
                        im = im.crop(CropLeftRightExcess)
                elif letter == 'C':
                    if digit <= 4:
                        im = im.crop((25, 0, 265, 240))
                    else:
                        im = im.crop((62, 0, 302, 240))
                elif letter == 'D' or letter == 'E':
                    if digit <= 4:
                        im = im.crop(CropRightExcess)
                    else:
                        im = im.crop(CropLeftRightExcess)
                elif letter == 'F':
                    if digit <= 4:
                        im = im.crop((17, 0, 257, 240))
                    else:
                        im = im.crop((60, 0, 300, 240))
                elif letter == 'G':
                    if digit <= 4:
                        im = im.crop((10, 0, 250, 240))
                    else:
                        im = im.crop((71, 0, 311, 240))
                elif letter == 'H':
                    if digit <= 4:
                        im = im.crop((35, 0, 275, 240))
                    else:
                        im = im.crop((69, 0, 309, 240))
                elif letter == 'I':
                    if digit <= 4:
                        im = im.crop((16, 0, 256, 240))
                    else:
                        im = im.crop(CropLeftRightExcess)
                elif letter == 'K':
                    im = im.crop(CropRightExcess)
                elif letter == 'L':
                    if digit <= 4:
                        im = im.crop((15, 0, 255, 240))
                    else:
                        im = im.crop((55, 0, 295, 240))
                elif letter == 'X':
                    if digit <= 4:
                        im = im.crop(CropRightExcess)
                    else:
                        im = im.crop((60, 0, 300, 240))
                else:
                    if digit <= 4:
                        im = im.crop(CropRightExcess)
                    else:
                        im = im.crop(CropLeftRightExcess)
            elif i == 8:
                if digit <= 4:
                    if letter == 'A':
                        im = im.crop(CropLeftRightExcess)
                    elif letter < 'E':
                        im = im.crop(CropLeftExcess)
                    elif letter < 'H':
                        im = im.crop(CropLeftRightExcess)
                    elif letter == 'H' or letter == 'I':
                        im = im.crop(CropLeftExcess)
                    elif letter < 'T':
                        im = im.crop(CropLeftRightExcess)
                    else:
                        im = im.crop(CropLeftExcess)
                else:
                    im = im.crop(CropRightExcess)

            elif i == 9:
                if letter == 'A':
                    if digit <= 4:
                        im = im.crop((47, 0, 287, 240))
                    else:
                        im = im.crop(CropLeftExcess)
                elif letter < 'D':
                    if digit <= 4:
                        im = im.crop((63, 0, 303, 240))
                    else:
                        im = im.crop(CropLeftExcess)
                elif letter < 'K':
                    im = im.crop(CropLeftExcess)
                else:
                    im = im.crop(CropLeftRightExcess)
            im.save(croppingWriteDir + str(i) + "/" + filename)

def SortImagesByLetter():
    hashmap = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    for i in range(3, 10):
        directory = croppingWriteDir + str(i)
        for filename in os.listdir(directory):
            letter = str(filename)[0]
            im = Image.open(directory + "/" + filename, 'r')
            hashmap[letter] += 1
            writeDir = sortingWriteDir + letter + "/"
            if not os.path.exists(writeDir):
                os.makedirs(writeDir)
            im.save(writeDir + letter + str(hashmap[letter]) + ".jpg")


Crop_Modify_Img()
SortImagesByLetter()