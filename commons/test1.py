from searchColorStripes import searchColorStripes
import io

#Load the image
#img = Image.open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues.jpg', 'r')
#f = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues.jpg', "rb")
#f2 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues2.jpg', "rb")
#f3 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues3.jpg', "rb")
f4 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\PHOTO-2020-06-06-17-16-11.jpg', "rb")
f5 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\PHOTO-2020-04-02-16-45-50.jpg', "rb")
f6 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_24-06-2020-2.jpg', "rb")
f7 = open('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_24-06-2020.jpg', "rb")

#farbcodes aus dem bild PHOTO-2020-04-02-16-45-50.jpg, welches unser spielbrett darstellt
# [ R x G x B; Standardabweichung zu R,G,B
#    (148.8469049373618, 155.67722918201915, 81.26261974944731, 19.137585941092834, 19.59442543222381, 11.041984054266281),
#    (120.34584723767149, 45.028364849833146, 60.55988134964775, 14.087531084921032, 9.28056944686372, 7.748086446983068),
#    (5.002989969135802, 85.58940972222223, 69.63310185185185, 8.45381029467554, 9.50608518754875, 8.485874243400707)
# ]  farbe 1: 149, 156, 81
#    farbe 2: 120, 45, 60
#    farbe 3: 5, 85, 69

# nach dem zweiten bild
# [
#   (146.41315427554406, 150.93706010840546, 79.4296577946768, 6.406236801106927, 12.05228327774037, 5.9526036700526905),
#   (118.81521739130434, 44.71974367293965, 60.074951330305, 4.27247650232333, 5.378924167525604, 4.313568691916516),
#   (7.935232282129536, 83.5567989148864, 69.05917260088165, 8.80010037907307, 5.801848126812544, 3.2294582973315284)
# ] farbe 1: 147, 151, 79
#   farbe 2: 119, 45, 60
#   farbe 3: 8, 83, 69

# nur das zweite bild
# [
#   (128.8578073089701, 116.74485049833888, 66.20797342192691, 5.37420755274795, 4.892330603281226, 10.780192994991337),
#   (108.09285714285714, 42.55779220779221, 56.67792207792208, 5.581958497508124, 15.06449029515864, 11.722280078026362),
#   (29.224789915966387, 68.79901960784314, 64.8921568627451, 13.655137304904995, 7.763274464514341, 8.29385855592572)
#]  farbe 1: 128, 117, 66
#   farbe 2: 108, 42, 56
#   farbe 3: 29, 69, 65

#[(128.8578073089701, 116.74485049833888, 66.20797342192691, 5.37420755274795, 4.892330603281226, 10.780192994991337),
#(108.09285714285714, 42.55779220779221, 56.67792207792208, 5.581958497508124, 15.06449029515864, 11.722280078026362),
#(29.224789915966387, 68.79901960784314, 64.8921568627451, 13.655137304904995, 7.763274464514341, 8.29385855592572)]
#[(148.8469049373618, 155.67722918201915, 81.26261974944731, 19.137585941092834, 19.59442543222381, 11.041984054266281),
#(120.34584723767149, 45.028364849833146, 60.55988134964775, 14.087531084921032, 9.28056944686372, 7.748086446983068),
#(5.002989969135802, 85.58940972222223, 69.63310185185185, 8.45381029467554, 9.50608518754875, 8.485874243400707)]
#[(146.41315427554406, 150.93706010840546, 79.4296577946768, 6.406236801106927, 12.05228327774037, 5.9526036700526905),
#(118.81521739130434, 44.71974367293965, 60.074951330305, 4.27247650232333, 5.378924167525604, 4.313568691916516),
#(7.935232282129536, 83.5567989148864, 69.05917260088165, 8.80010037907307, 5.801848126812544, 3.2294582973315284)]


scs = searchColorStripes(newRgbToleranze=7,
    newMaxPixelBetweenXHits=24,
    newMaxPixelBetweenYHits=24,
    newCropPercentage=0.2,
    newDebug=True,
    newFirstColor=(123, 112, 56),
    newSecondColor=(103, 27, 45),
    newThirdColor=(39, 61, 56),
    newFirstColor2=(164, 171, 89),
    newSecondColor2=(135, 55, 68),
    newThirdColor2=(7, 95, 78))

#img1 = scs.drawBlackLinesOnImg(f)
#img2 = scs.drawBlackLinesOnImg(f2)
#print(scs.distanceFromImgCenter(f2))
#img3 = scs.drawBlackLinesOnImg(f3)
#print(img3[1])
img4 = scs.drawBlackLinesOnImg(f4)
print(img4[1])
img5 = scs.drawBlackLinesOnImg(f5)
print(img5[1])
img6 = scs.drawBlackLinesOnImg(f6)
print(img6[1])
img7 = scs.drawBlackLinesOnImg(f7)
print(img7[1])
#f.close()
#f2.close()
#f3.close()
f4.close()
f5.close()
f6.close()
f7.close()
#img1.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues_cross.jpg')
#img2.save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues2_cross.jpg')
#img3[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\trust_issues3_cross.jpg')
#img4[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_colors_from_pi_1.jpg')
img4[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\PHOTO-2020-06-06-17-16-11-test.jpg')
img5[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\PHOTO-2020-04-02-16-45-50-test.jpg')
img6[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_24-06-2020-2-test.jpg')
img7[0].save('C:\\Users\\lasse\\github\\SS_20_Robotik_T01\\cameraTestImages\\test_24-06-2020-test.jpg')
