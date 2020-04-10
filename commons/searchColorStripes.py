from PIL import Image
import math
import statistics

class searchColorStripes(object):

    #------ CONFIG
    cropPercentage = 0.1 # 10% of Image will be ignored (total of x * 2 %, top part and bottom part are cropped)
    rgbToleranze = 20 # measures if a color is within a certain range (x1 - t <= x2 <= x1 + t) for each RGB Value
    maxPixelBetweenXHits = 2 # allowed amount between two pixel-hits on x-coodinate
                            # 1 = no pixel in between two hits
                            # 2 = 1 pixel in between hits
                            # 10 = 9 pixels inbetween hits, a.s.f.
    maxPixelBetweenYHits = 10 # allowed amount between two pixel-hits on y-coodinate

    #        r, g, b
    frstC = (238, 26, 38)
    scndC = (33, 178, 77)
    thrdC = (0, 162, 234)

    debug = False
    #------ CONFIG

    #default
    def __init__(self, newCropPercentage=0.1, newRgbToleranze=20, newMaxPixelBetweenXHits=2, newMaxPixelBetweenYHits=10, newFirstColor=(238, 26, 38), newSecondColor=(33, 178, 77), newThirdColor=(0, 162, 234), newDebug = False):
        self.debug = newDebug
        if self.debug : print('I\'m ready!')
        self.cropPercentage = newCropPercentage
        self.rgbToleranze = newRgbToleranze
        self.maxPixelBetweenXHits = newMaxPixelBetweenXHits
        self.maxPixelBetweenYHits = newMaxPixelBetweenYHits
        self.frstC = newFirstColor
        self.scndC = newSecondColor
        self.thrdC = newThirdColor
        if self.debug : print('CONFIG: CP: %s RGB-T: %s MPX: %s MPY: %s C1: %s C2: %s C3: %s '%(self.cropPercentage, self.rgbToleranze, self.maxPixelBetweenXHits, self.maxPixelBetweenYHits, self.frstC, self.scndC, self.thrdC))

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
    # returns a tuple of (boolean, firstY, lastY, ordered sequence of colors)
    #  where first param represents a success, second and 3rd param the y-coordinates
    #    where the first and last pixel color hit accured
    def findTreeColorStripesInARow(self, height, pix_val, x):
        cropVal = math.floor(height * self.cropPercentage)
        firstHits = 0
        secondHits = 0
        thirdHits = 0
        # each following attribute represents an y-coordinate of the first and
        # last hit of one of the colors.
        fstHitOfFstColor = -1
        lastHitOfFstColor = -1
        fstHitOfSndColor = -1
        lastHitOfSndColor = -1
        fstHitOfTrdColor = -1
        lastHitOfTrdColor = -1
        #contains the number of the Colors in wich order they where found in the pixels
        orderOfColors = []
        # foreach is from top to bottom of the image, REDUCED by % (configured cropPercentage in) of the image size
        fromY = int(math.floor(0 + cropVal))
        toY = int(math.floor(height - cropVal - 1))
        for y in range(fromY, toY):
            thisPixel = pix_val[x,y]
            nextPixel = pix_val[x,y]
            # if this pixel and next pixel match a color, increase amount of total hits of that representive color
            # if the first hit y-coordinate is not set ( eq. -1) set it to the first y of that representive color
            # always sets the last y-coodinate of that color to the last y found
            # also increases the total amount of pixels found of one color
            if self.compareColors(self.frstC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.frstC, nextPixel,self. rgbToleranze):
                    if fstHitOfFstColor == -1:
                        orderOfColors.append(1)
                        fstHitOfFstColor = y
                    lastHitOfFstColor = y
                    firstHits += 1
            if self.compareColors(self.scndC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.scndC, nextPixel, self.rgbToleranze):
                    if fstHitOfSndColor == -1:
                        orderOfColors.append(2)
                        fstHitOfSndColor = y
                    lastHitOfSndColor = y
                    secondHits += 1
            if self.compareColors(self.thrdC, thisPixel, self.rgbToleranze):
                if self.compareColors(self.thrdC, nextPixel, self.rgbToleranze):
                    if fstHitOfTrdColor == -1:
                        orderOfColors.append(3)
                        fstHitOfTrdColor = y
                    lastHitOfTrdColor = y
                    thirdHits += 1
        #end for

        # add all y-coordinates (first and last pixel-hit) to an list. if one color is missing, the list contains at least one -1 value
        arrayHits = [fstHitOfFstColor, lastHitOfFstColor, fstHitOfSndColor, lastHitOfSndColor, fstHitOfTrdColor, lastHitOfTrdColor]
        # if so, it is not a correct 3-conclusive color stripe
        if -1 in arrayHits:
            if self.debug : print('at least one color did not show up %s '%(arrayHits) )
            return (False, -1, -1, orderOfColors)

        # measuring the total distance between the first color hit and the last
        # to compare the total amount of all pixel of each color found
        maxY = max(arrayHits)
        minY = min(arrayHits)
        distanceFirstAndLastHit = maxY - minY
        distancePixelAmount = firstHits + secondHits + thirdHits

        # if the pixel amount of hits is far greater then the distance between first and last hit,
        # there probably is some color rustle in the background going on, therefore the total pixel amount
        # must not be more then x pixels of different color apart from the first and last hit.
        if distancePixelAmount + self.maxPixelBetweenYHits >= distanceFirstAndLastHit:
            if self.debug : print('did a hit at x: %s hits, but measure did not fit first: %s last: %s distance: %s - %s, order of colors: %s'%(x, minY, maxY, distanceFirstAndLastHit, distancePixelAmount, orderOfColors))
            return (True, minY, maxY, orderOfColors)

        return (False, maxY, minY, orderOfColors)

    def createResultTupel(self, firstX, lastX, imgWidth, avarageY, orderOfColors):
        half = 0
        if imgWidth % 2 > 1:
            half = (imgWidth -1) / 2
        else:
            half = imgWidth / 2
        x1Percentage = (firstX-half)/half
        x2Percentage = (lastX-half)/half
        avarageXPercentage = (x1Percentage + x2Percentage) / 2
        newTupel = (x1Percentage, x2Percentage, avarageXPercentage, firstX, lastX, avarageY, orderOfColors)
        if self.debug : print('creating new result x1-%%: %s x2-%%: %s avarage-x-%%: %s x1: %s x2: %s avarage-y: %s, order of colors %s '%newTupel)
        return newTupel


    # this function scans the image content pixel by pixel and returns a list of tupels, which contain informations about
    # three color stripes following each other
    #
    # result tupel format: (first-X-%, last-X-%, avarage-X-%, first-X, last-X, avarage-Y')
    # first-X Percentage, measured with the total width of the Image
    #   ranges between -1 and 1, because its calculated from the image-center
    #       therefore close to -1 = left side of image
    #                 close to  1 = right side of image
    #                 close to  0 = close to image center
    # same goes for last-X Percentage and avarage X Percentage
    # first-X : Pixel of the first X hit
    # last-X : Pixel of the last X hits
    # avarage-Y: Pixel avarage of all Y hits
    #
    # example Result: [(0.6173913043478261, 0.8826086956521739, 0.75, 372, 433, 108.5, [1, 2, 3])]
    def distanceFromImgCenter(self, f):
        img = Image.open(f)
        pix_val = img.load()

        height = img.size[1]
        width = img.size[0]
        if self.debug : print('Image opend; width: %s, height: %s'%(width,height))
        resultList = []
        # moves along the x-coordinates of the image and checks if a range of pixels from the y-coordinates
        # do contain the tree colors defined with frstC, scndC and thrdC
        for x in range(0, width):
            retVal = self.findTreeColorStripesInARow(math.floor(height), pix_val, x)
            if retVal[0] == True:
                newTupel = (x, retVal)
                resultList.append(newTupel)
        # result list of format: (x-coordinate (boolean, firstY-coordinate, lastY-coordinate, ordered sequence of colors ))
        # if results are empty return early
        if len(resultList) == 0:
            if self.debug : print ('no results. early returning')
            return []
        # if resuluts are not empty, it is then sorted by x-coodinate
        colorStripeHits = sorted(resultList)
        colorStripeRange = []
        first = -1
        last = -1
        avarageYs = []
        lastColorSequence = []
        # iterates through all representive x- and y- Pixel Color hits and builds an avarage of the result List
        for i in range(0, len(colorStripeHits) -1):
            y1 = colorStripeHits[i][1][1]
            y2 = colorStripeHits[i][1][2]
            avarageY = (y1+y2)/2
            #contains every avarage y,
            avarageYs.append(avarageY)

            thisHit = colorStripeHits[i][0]
            nextHit = colorStripeHits[i+1][0]
            #checking if the conceclusive x- hits are no more then x pixels apart (maxPixelBetweenXHits config)
            if thisHit - self.maxPixelBetweenXHits < nextHit < thisHit + self.maxPixelBetweenXHits :
                last = colorStripeHits[i][0]
                lastColorSequence = colorStripeHits[i][1][3]
                if first == -1:
                    first = colorStripeHits[i][0]
            else:
                # result tupel format: (first-X-%, last-X-%, avarage-X-%, first-X, last-X, avarage-Y')
                # first-X Percentage, measured with the total width of the Image
                #   ranges between -1 and 1, because its calculated from the image-center
                #       therefore close to -1 = left side of image
                #                 close to  1 = right side of image
                #                 close to  0 = close to image center
                # same goes for last-X Percentage and avarage X Percentage
                # first-X : Pixel of the first X hit
                # last-X : Pixel of the last X hits
                # avarage-Y: Pixel avarage of all Y hits
                if self.debug : print (avarageYs)
                colorStripeRange.append(self.createResultTupel(first, last, width, statistics.mean(avarageYs), lastColorSequence))
                avarageYs = []
                first = -1
                last = -1
        #last pixel hit wont be captured in for-iteration, so last result is added here
        if self.debug : print (avarageYs)
        colorStripeRange.append(self.createResultTupel(first, last, width, statistics.mean(avarageYs), lastColorSequence))

        return colorStripeRange

    def drawBlackLinesOnImg(self, f):
        debugTemp = self.debug
        self.debug = False
        img = Image.open(f)

        #Get basic details about the image
        print(img.format)
        print(img.mode)
        print(img.size)

        pix_val = img.load()

        print(pix_val[10,10])

        height = img.size[1]
        width = img.size[0]

        print('width: %s height: %s '%(width, height))

        results = self.distanceFromImgCenter(f)
        for x in range(0, width):
            retVal = self.findTreeColorStripesInARow(height, pix_val, x)
            if retVal[0] == True:
                #paintItBlack
                pix_val[x, retVal[1]] = (0,0,0)
                pix_val[x, retVal[2]] = (0,0,0)

        #paint a black cross in hits
        #example: [(0.6173913043478261, 0.8826086956521739, 0.75, 372, 433, 108.5)]
        for res in results:
            avarageX = math.floor((res[3]+res[4])/2)
            avarageY = math.floor(res[5])
            for i in range(avarageX-10, avarageX+10):
                pix_val[i, avarageY] = (0,0,0)
            for j in range(avarageY-10, avarageY+10):
                pix_val[avarageX, j] = (0,0,0)

        #show the image
        img.show()
        theResult = (img, results)
        self.debug = debugTemp
        return theResult
    #end drawBlackLinesOnImg
