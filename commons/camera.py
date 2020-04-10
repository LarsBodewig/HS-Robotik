from searchColorStripes import searchColorStripes
from picamera import PiCamera
from io import BytesIO

class Camera(object):

    def __init__(self):
        self.piCamera = PiCamera()
        self.piCamera.resolution = (1024, 768)
        self.scs = searchColorStripes(newRgbToleranze=30,
            newMaxPixelBetweenXHits=4,
            newDebug=False,
            newFirstColor=(149, 156, 81),
            newSecondColor=(120, 45, 60),
            newThirdColor=(5, 85, 69))

    def captureImage(self):
        my_stream = BytesIO()
        #self.piCamera.start_preview()
        #sleep(2)
        self.piCamera.capture(my_stream, 'jpeg')
        #self.piCamera.stop_preview()
        return my_stream

    def searchCorners(self):
        return self.scs.distanceFromImgCenter(self.captureImage())
