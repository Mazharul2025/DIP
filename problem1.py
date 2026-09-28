import cv2

gray_image = cv2.imread("a1.jpeg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Grayscale Image", gray_image)

height, width = gray_image.shape

print("Gray Image")
print("Width:", width, "pixels")
print("Height:", height, "pixels")
print("Number of Channels: 1")
print("Data Type:", gray_image.dtype)
print("Data Type Description: 8-bit unsigned integer")

cv2.waitKey(0)
cv2.destroyAllWindows()


color_image = cv2.imread("a1.jpeg", cv2.IMREAD_COLOR)

cv2.imshow("Color Image", color_image)

height, width, channels = color_image.shape

print("\nColor Image")
print("Width:", width, "pixels")
print("Height:", height, "pixels")
print("Number of Channels:", channels)
print("Data Type:", color_image.dtype)
print("Data Type Description: 8-bit unsigned integer")

cv2.waitKey(0)
cv2.destroyAllWindows()