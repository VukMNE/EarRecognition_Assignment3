import cv2
import numpy as np
import json
import glob
from PIL import Image



# with open('config.json') as config_file:
#   config = json.load(config_file)

train_path = '../data/crop_train'
im_list = sorted(glob.glob(train_path + '/*.png', recursive=True))



for im_name in im_list:
  thename = im_name.split('\\')[-1]
  img = cv2.imread(im_name)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  size = (96,96)
  img = cv2.resize(img, size)
  print(thename)
  cv2.imwrite('C:\\biometrics\\assignment3\\data\\nn_train\\' + thename, img)


test_path = '../data/crop_test'
im_list = sorted(glob.glob(test_path + '/*.png', recursive=True))



for im_name in im_list:
  thename = im_name.split('\\')[-1]
  img = cv2.imread(im_name)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  size = (96,96)
  img = cv2.resize(img, size)
  print(thename)
  cv2.imwrite('C:\\biometrics\\assignment3\\data\\nn_test\\' + thename, img)

print('Program finished...')








