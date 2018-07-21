# -*- coding:utf-8 -*-
# Program:
#		replace the video with character
# Release:
#		2018/07/21	ZhangDao	First release
import cv2

try:
	from . import convertImage
except:
	import convertImage

def solve(name):
	'''main function to convert the video
	Args:
		name:	name of video to convert
	Returns:
		None
	'''
	videoCapture = cv2.VideoCapture(name)
	fps = videoCapture.get(cv2.CAP_PROP_FPS)
	size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
		int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
	videoWriter = cv2.VideoWriter(
		'output.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), 
		fps, size)

	success, frame = videoCapture.read()
	count = 1
	while success:	# Loop until there are no more frames.
		# print (frame.shape)	# (640, 368, 3)
		print ('frame %d:\t%s' % (count, success))
		frame = convertImage.convertImage(frame, False)
		videoWriter.write(frame)
		success, frame = videoCapture.read()
		count += 1

if __name__ == '__main__':
	solve('wangzhe.mp4')