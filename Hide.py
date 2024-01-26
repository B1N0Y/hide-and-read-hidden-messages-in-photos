from LSBSteg import *

#encoding
steg = LSBSteg(cv2.imread("koro.jpeg"))
img_encoded = steg.encode_text("Hello World")
cv2.imwrite("my_new_image.png", img_encoded)