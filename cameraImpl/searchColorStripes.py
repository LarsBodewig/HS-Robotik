
from PIL import Image
import math


class searchColorStripes(object):

    #------ CONFIG
    cropPercentage = 0.1 # 10% of Image will be ignored (total of x * 2 %, top part and bottom part are cropped)
    rgbToleranze = 20 # measures if a color is within a certain range (x1 - t <= x2 <= x1 + t) for each RGB Value

    #        r, g, b
    frstC = (238, 26, 38)
    scndC = (33, 178, 77)
    thrdC = (0, 162, 234)
    #------ CONFIG


    #default example:
    def __init__(self, newCropPercentage=0.1, newRgbToleranze=20, newFirstColor=(238, 26, 38), newSecondColor=(33, 178, 77), newThirdColor=(0, 162, 234)):
        print('I\'m ready!')
        self.cropPercentage = newCropPercentage
        self.rgbToleranze = newRgbToleranze
        self.frstC = newFirstColor
        self.scndC = newSecondColor
        self.thrdC = newThirdColor
        print('CONFIG: CP: %s RGB-T: %s C1: %s C2: %s C3: %s '%(self.cropPercentage, self.rgbToleranze, self.frstC, self.scndC, self.thrdC))

    # test for colors within the same range tested by toleranze
    # also same value is an hit
    def compareColors(self, color1, color2, toleranze):
        r1 = color1[0]
        g1 = color1[1]
        b1 = color1[2]
        r2 = color2[0]
        g2 = color2[1]
        b2 = color2[2]
        if (r1-toleranze <= r2 <= r1+toleranze) and (g1-toleranze <= g2 <= g1+toleranze) and (b1-toleranze <= b2 <= b1+toleranze):
            return True
        return False

    def findTreeColorStripesInARow(self, height, pix_val, x):
        cropVal = math.floor(height * self.cropPercentage)

        firstHits = 0
        secondHits = 0
        thirdHits = 0

        fstHitOfFstColor = -1
        lastHitOfFstColor = -1
        fstHitOfSndColor = -1
        lastHitOfSndColor = -1
        fstHitOfTrdColor = -1
        lastHitOfTrdColor = -1

        #foreach is from top to bottom if the image, reduced by % of image size
        for y in range(0 + cropVal, height - cropVal - 1):
            thisPixel = pix_val[x,y]
            nextPixel = pix_val[x,y]

            #if this pixel and next pixel math a color, increase amount of total hits of that representive color
            if self.compareColors(self.frstC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.frstC, nextPixel,self. rgbToleranze):
                    if fstHitOfFstColor == -1:
                        fstHitOfFstColor = y
                    lastHitOfFstColor = y
                    firstHits += 1
            if self.compareColors(self.scndC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.scndC, nextPixel, self.rgbToleranze):
                    if fstHitOfSndColor == -1:
                        fstHitOfSndColor = y
                    lastHitOfSndColor = y
                    secondHits += 1
            if self.compareColors(self.thrdC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.thrdC, nextPixel, self.rgbToleranze):
                    if fstHitOfTrdColor == -1:
                        fstHitOfTrdColor = y
                    lastHitOfTrdColor = y
                    thirdHits += 1

        #end for
        arrayHits = [fstHitOfFstColor, lastHitOfFstColor, fstHitOfSndColor, lastHitOfSndColor, fstHitOfTrdColor, lastHitOfTrdColor]

        if -1 in arrayHits:
            #print('at least one color did not show up %s '%(arrayHits) )
            return (False, -1, -1)

        maxY = max(arrayHits)
        minY = min(arrayHits)

        distancePoints = maxY - minY
        distanceHits = firstHits + secondHits + thirdHits

        #if the pixel amount of hits is far greater then the distance between first and last hit,
        #it is probably some color ruslte in the background going on
        if distanceHits <= distanceHits:
            #print('did a hit at x: %s hits, but measure did not fit first: %s last: %s distance: %s : %s '%(x, minY, maxY, distancePoints, distanceHits))
            return (True, minY, maxY)

        return (False, maxY, minY)

    def drawBlackLinesOnImg(self, f):
        img = Image.open(f)

        #Get basic details about the image
        print(img.format)
        print(img.mode)
        print(img.size)

        pix_val = img.load()

        print(pix_val[10,10])

        height = img.size[1]
        width = img.size[0]
        half = 0

        print('width: %s height: %s '%(width, height))

        if width % 2 > 1:
            half = math.floor((width -1)/2)
        else:
            half = math.floor(width / 2)

        for x in range(0, width):
            retVal = self.findTreeColorStripesInARow(height, pix_val, x)
            if retVal[0] == True:
                #paintItBlack
                pix_val[x, retVal[1]] = (0,0,0)
                pix_val[x, retVal[2]] = (0,0,0)

        #show the image
        img.show()
