import cv2
image = cv2.imread('yay.jpg')

start = (100,100)
end = (100, 500)
color = (355, 0, 255)
thickness = 2

image = cv2.line(image, start, end, color, thickness)

cv2.imshow('Line', image)
cv2.waitKey(0)
cv2.destroyAllWindows()