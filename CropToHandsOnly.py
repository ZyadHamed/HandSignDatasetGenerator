import numpy as np
from PIL import Image
import mediapipe as mp
import os

#Variables you should tweak to your personal interest (the code assumes the sortingReadDir is the same as croppingWriteDir
croppingReadDir = "Dataset/user_"
croppingWriteDir = "HandsOnlyColored/user_"
sortingWriteDir = "HandsOnlyColoredFinal/"
GrayScale = False

mpHands = mp.solutions.hands
hands = mpHands.Hands(static_image_mode=False,
                      max_num_hands=1,
                      min_detection_confidence=0.4,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils


def Crop_Modify_Img():
    for i in range(3, 10):
        directory = croppingReadDir + str(i)
        for filename in os.listdir(directory):
            letter = str(filename)[0]
            digit = int(str(filename)[1])
            img = Image.open(directory + "/" + filename, 'r')
            img = np.array(img)
            height, width, c = img.shape
            results = hands.process(img)
            # Basic maximum and minimum algorithm, intitalize max to 0 and min to maxmium value
            x_min = width
            x_max = 0
            y_min = height
            y_max = 0
            # Loop on the hands landmarks (1 hand for now)
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLms.landmark):  # Loop on each landmark
                        # The actual x and y of the landmark (as opposed to the ratio outputted by the library)
                        cx, cy = int(lm.x * width), int(lm.y * height)
                        # Update the max and min values whenever needed
                        x_min = min(x_min, cx)
                        x_max = max(x_max, cx)
                        y_min = min(y_min, cy)
                        y_max = max(y_max, cy)
                    # Form a square around the hand and maximize the area of that square
                    if (y_max - y_min > x_max - x_min):
                        # The hand is oriented vertically (the difference between the furthest y_coordinates is larger than that of the x_coordinates)
                        # the Set the side_length of the square to the difference between the 2 y_coordinates and add 50 to include bits of the hand outside the landmarks
                        side_length = y_max - y_min + 50
                        # The remaining length to be added to the x_coordinates from both right and left to make the distance between them the same as the distance between y_coordinates (a square)
                        margin_addition = (side_length - (x_max - x_min)) / 2
                        # Add the margin_addition from left and right, include the 50 added to side_length in the y_coordinate calculation
                        margin_addition = (side_length - (x_max - x_min)) / 2
                        totalPoint = (int(x_min - margin_addition), y_min - 25, int(x_max + margin_addition), y_max + 25)
                    else:
                        # The hand is oriented horizontally (the difference between the furthest x_coordinates is larger than that of the y_coordinates)
                        # Similar algorithm as above
                        side_length = x_max - x_min + 50
                        margin_addition = (side_length - (y_max - y_min)) / 2
                        # Make a rectangle from the estimated points that would make the best possible square
                        totalPoint = (x_min - 25, int(y_min - margin_addition) , x_max + 25, int(y_max + margin_addition))
            #A problem happened using the hands classifcation, this handles this exception
            if totalPoint == ():
                continue
            #Crop the dataset image in question using the calculated square area, resize it, and save it to the writeDir
            img = Image.fromarray(img)
            img = img.crop(totalPoint)
            img = img.resize((224, 224))

            img.save(croppingWriteDir + str(i) + "/" + filename)

#Sort the dataset images into folders, each with the name of the class (A, B, C, etc)
def SortImagesByLetter():
    hashmap = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    for i in range(3, 10):
        directory = "HandsOnlyColored/user_" + str(i)
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