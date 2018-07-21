## pic2char
Functions to replace the picture with character

# Source image is:

![pic](./baoerjie.jpg)

# After the process, the image is:

![pic](./output.jpg)

# method
Use cv2.Canny to detect edge, and paint charater '1' on the edge of a black image.

## usage
1.replace the picture with character
```Shell
python convertImage.py
```
2.replace the video with character
```Shell
python convertVideo.py
```
## future work
The video produced is mute, I'll add the audio to the video when I'm free.
