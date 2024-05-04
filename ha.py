import cv2
image = cv2.imread('yay.jpg')

start = (200,100)
end = (200, 200)
end2 = (200,0)
color = (255, 0, 255)
thickness = 2

cv2.rectangle(image, (100,100),(400,300),(0,0,0), -1)
cv2.line(image, (100,100),(200,0),color,thickness)
cv2.line(image, (400,100),(200,0),color,thickness)

cv2.imshow('Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()