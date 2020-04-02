from searchColorStripes import searchColorStripes
import io

#Load the image
#img = Image.open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues.jpg', 'r')
f = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues.jpg', "rb")
f2 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues2.jpg', "rb")

scs = searchColorStripes(newDebug=False)

img1 = scs.drawBlackLinesOnImg(f)
img2 = scs.drawBlackLinesOnImg(f2)
f.close()
f2.close()
img1.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues_cross.jpg')
img2.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraImpl\\trust_issues2_cross.jpg')
