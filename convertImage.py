# -*- coding:utf-8 -*-
# Program:
#		replace the picture with character
# Release:
#		2018/07/21	ZhangDao	First release
import cv2
import numpy as np

def convertImage(img, ifShow=False):
	'''main function to convert the picture
	Args:
		img:	img of numpy type
		ifShow:	if show the result
	Returns:
		None
	'''
	# canny edge detection
	imgCanny = cv2.Canny(img, 200, 300)
	# print (imgCanny.shape)# (192, 263)

	# get size of the image
	h, w, d = img.shape
	# print (h, w, d)# (478, 342, 3)

	# a blank picture
	imgBlank = np.zeros((h, w, d), np.uint8)

	dpi = 5
	font = cv2.FONT_HERSHEY_SIMPLEX
	threshold = 1
	for i in range(0, h-dpi, dpi):
		for j in range(0, w-dpi, dpi):
			sum = 0.0
			for k in range(i, i+dpi):
				for l in range(j, j+dpi):
					sum += imgCanny[k][l]
			if (ifShow):
				print (sum)
			if sum < threshold:
				# continue
				cv2.putText(imgBlank, '1', (j, i), font, 0.1, (0, 255, 0), 1, False)
			else:
				continue
				cv2.putText(imgBlank, '0', (j, i), font, 0.1, (0, 255, 0), 1, False)

	# save and show
	if (ifShow):
		# save
		cv2.imwrite('output.jpg', imgBlank, [int( cv2.IMWRITE_JPEG_QUALITY), 95])
	
		# show
		cv2.imshow('image', imgBlank)
		cv2.waitKey()
		cv2.destroyWindow('image')
	else:
		return imgBlank


if __name__ == '__main__':
	img = cv2.imread('baoerjie.jpg')
	convertImage(img, True)

	# img = cv2.imread('baoerjie2.jpeg')
	# convertImage(img, True)