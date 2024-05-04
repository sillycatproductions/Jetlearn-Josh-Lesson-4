import cv2
image = cv2.imread('yay.jpg')

font = cv2.FONT_ITALIC
pos = (350,100)
font_scale = 1
color = (0,0,0)
thickness = 2

image = cv2.putText(image, 'silly goober :3', pos, font, font_scale, color, thickness)

cv2.imshow('Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()