from picamera import PiCamera
from io import BytesIO

class Camera(object):

    def __init__(self):
        self.piCamera = PiCamera()
        self.piCamera.resolution = (1024, 768)

    def captureImage(self):

        my_stream = BytesIO()
        #self.piCamera.start_preview()
        #sleep(2)
        self.piCamera.capture(my_stream, 'jpeg')
        #self.piCamera.stop_preview()
        return my_stream
