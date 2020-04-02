from PIL import Image
import math
import statistics

def ImageGetColorAndStdDev(img):
    pix_val = img.load()
    width = img.size[0]
    height = img.size[1]
    totalAmount = 0;
    averageR = 0
    averageG = 0
    averageB = 0
    for i in range (0, width):
        for j in range(0,height):
            averageR += pix_val[i,j][0]
            averageG += pix_val[i,j][1]
            averageB += pix_val[i,j][2]
            totalAmount += 1
    averageR = averageR / totalAmount
    averageG = averageG / totalAmount
    averageB = averageB / totalAmount

    print(totalAmount)
    print(averageR)
    print(averageG)
    print(averageB)

    stdDeviationR = 0
    stdDeviationG = 0
    stdDeviationB = 0
    sumR = 0
    sumG = 0
    sumB = 0
    for i in range (0, width):
        for j in range(0,height):
            sumR += math.pow(pix_val[i,j][0] - averageR, 2)
            sumG += math.pow(pix_val[i,j][1] - averageG, 2)
            sumB += math.pow(pix_val[i,j][2] - averageB, 2)
    stdDeviationR = math.sqrt(sumR/totalAmount)
    stdDeviationG = math.sqrt(sumG/totalAmount)
    stdDeviationB = math.sqrt(sumB/totalAmount)
    return (averageR,averageG,averageB,stdDeviationR,stdDeviationG,stdDeviationB)

f1 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\Yellow_1.png', "rb")
f2 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\Red_1.png', "rb")
f3 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\Green_1.png', "rb")

imgColor1 = Image.open(f1)
imgColor2 = Image.open(f2)
imgColor3 = Image.open(f3)

newRgbCodes = [ImageGetColorAndStdDev(imgColor1),ImageGetColorAndStdDev(imgColor2),ImageGetColorAndStdDev(imgColor3)]
f1.close()
f2.close()
f3.close()
print(newRgbCodes)
