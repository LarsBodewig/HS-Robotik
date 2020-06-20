from .searchColorStripes import searchColorStripes
from picamera import PiCamera
from io import BytesIO

class Camera(object):

    def __init__(self):
        self.piCamera = PiCamera()
        self.piCamera.resolution = (1024, 768)
        self.scs = searchColorStripes(newRgbToleranze=7,
            newMaxPixelBetweenXHits=24,
            newMaxPixelBetweenYHits=24,
            newCropPercentage=0.2,
            newFirstColor=(123, 112, 56),
            newSecondColor=(103, 27, 45),
            newThirdColor=(39, 61, 56),
            newFirstColor2=(164, 171, 89),
            newSecondColor2=(135, 55, 68),
            newThirdColor2=(7, 95, 78))

    def captureImage(self):
        my_stream = BytesIO()
        #self.piCamera.start_preview()
        #sleep(2)
        self.piCamera.capture(my_stream, 'jpeg')
        #self.piCamera.stop_preview()
        return my_stream

    def searchCorners(self):
        return self.scs.distanceFromImgCenter(self.captureImage())
