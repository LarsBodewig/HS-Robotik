from searchColorStripes import searchColorStripes
import io

#Load the image
#img = Image.open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues.jpg', 'r')
#f = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues.jpg', "rb")
#f2 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues2.jpg', "rb")
#f3 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues3.jpg', "rb")
f4 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\PHOTO-2020-04-02-16-45-50.jpg', "rb")

#farbcodes aus dem bild PHOTO-2020-04-02-16-45-50.jpg, welches unser spielbrett darstellt
# [ R x G x B; Standardabweichung zu R,G,B
#    (148.8469049373618, 155.67722918201915, 81.26261974944731, 19.137585941092834, 19.59442543222381, 11.041984054266281),
#    (120.34584723767149, 45.028364849833146, 60.55988134964775, 14.087531084921032, 9.28056944686372, 7.748086446983068),
#    (5.002989969135802, 85.58940972222223, 69.63310185185185, 8.45381029467554, 9.50608518754875, 8.485874243400707)
# ]  farbe 1: 149, 156, 81
#    farbe 2: 120, 45, 60
#    farbe 3: 5, 85, 69

scs = searchColorStripes(newRgbToleranze=30,
    newMaxPixelBetweenXHits=4,
    newDebug=False,
    newFirstColor=(149, 156, 81),
    newSecondColor=(120, 45, 60),
    newThirdColor=(5, 85, 69))

#img1 = scs.drawBlackLinesOnImg(f)
#img2 = scs.drawBlackLinesOnImg(f2)
#print(scs.distanceFromImgCenter(f2))
#img3 = scs.drawBlackLinesOnImg(f3)
#print(img3[1])
img4 = scs.drawBlackLinesOnImg(f4)
#f.close()
#f2.close()
#f3.close()
f4.close()
#img1.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues_cross.jpg')
#img2.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues2_cross.jpg')
#img3[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues3_cross.jpg')
img4[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_colors_from_pi_1.jpg')
