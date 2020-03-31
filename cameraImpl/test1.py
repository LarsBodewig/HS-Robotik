import math
from searchColorStripes import searchColorStripes

#Load the image
#img = Image.open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues.jpg', 'r')
f = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues.jpg', "rb")

scs = searchColorStripes()

scs.distanceFromImgCenter(f)
