'''
An weird problem I encounter is that when I use imread() in utils.py then plot the image I read in,it looks
quite strange and far from the real input.
The reason is that imread() function uses scipy.misc.imread() and calls astype(np.float) to change the returned 
ndarray dtype,which causes that weird-looking image.Further tests tell me that only when I use dtype=uint8 the 
plt.show() gives the result I want.Though using other dtypes won't change the array values but it causes unexpected
outcome.
'''
import scipy.misc
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from utils import *

cur_dir = os.getcwd()
test_dir = os.path.join(cur_dir,"data/test")

all_test_imgs = os.listdir(test_dir)
all_test_imgs = [os.path.join(test_dir,i) for i in all_test_imgs]
# print all_test_imgs[:5]
test_index = 15
test_img = all_test_imgs[test_index]

get_img = [get_image(test_img, 108, is_crop=True, resize_w=64, is_grayscale = 0) for i in range(10)]
print type(get_img)
get_img = np.array(get_img).astype(np.float32)
print type(get_img)
print get_img.shape

raw_img = imread(path = test_img, is_grayscale = False)
# raw_img = imread(path = test_img, is_grayscale = False).astype(np.uint8)
# raw_img = scipy.misc.imread(test_img).astype(np.float)
# raw_img = scipy.misc.imread(test_img)
# print raw_img.dtype
plt.imshow(raw_img)
plt.show()
# scipy.misc.imsave('test.png',raw_img)

# this also works pretty well
# img = mpimg.imread(test_img)
# print img.dtype
# plt.imshow(img)
# plt.show()


cropped_img = center_crop(raw_img,crop_h = 218,crop_w = 178,resize_w = 250)
# print(cropped_img.shape)
plt.imshow(cropped_img)
plt.show()
# print raw_img == img

# change pixel value range from [0,255] to [-1,1]
input_img = np.array(cropped_img)/127.5 - 1.  
plt.imshow(input_img)
plt.show()

