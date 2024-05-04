import cv2
image = cv2.imread('yay.jpg')
center_coordinates = (400,200)
radius = 40
color = (0, 0, 255)
thickness = 5

image = cv2.circle(image, center_coordinates, radius, color, thickness)

cv2.imshow('Circle', image)
cv2.waitKey(0)
cv2.destroyAllWindows()