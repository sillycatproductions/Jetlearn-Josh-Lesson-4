import cv2
image = cv2.imread('yay.jpg')

start = (5,5)
end = (100, 500)
color = (355, 0, 255)
thickness = -1

image = cv2.rectangle(image, start, end, color, thickness)

cv2.imshow('Rectangle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()