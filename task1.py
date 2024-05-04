import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("1.jpg")
color = ('blue', 'green', 'red')
for i, col in enumerate(color):
    hist = cv.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=col + " channel")

plt.xlim([0, 256])
plt.legend()
plt.title("Color Channel Histograms (Original)")
plt.show()

alpha = 2
beta = 30
Adjusted_Image = cv.convertScaleAbs(image, alpha=alpha,beta=beta)
plt.figure()
color = ('blue', 'green', 'red')

for i, col in enumerate(color):
    hist = cv.calcHist([Adjusted_Image], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=col + " channel")

    plt.xlim([0, 256])

cv.imshow("Adjusted Image", Adjusted_Image)
cv.waitKey(0)
cv.destroyAllWindows()
plt.show()