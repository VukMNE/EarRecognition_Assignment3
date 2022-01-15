import cv2
import numpy as np
import json
import glob



# with open('config.json') as config_file:
#   config = json.load(config_file)

images_path = 'data/crop_train'
im_list = sorted(glob.glob(images_path + '/*.png', recursive=True))

heights = list()
widths = list()

for im_name in im_list:
  img = cv2.imread(im_name)
  height, width, channel = img.shape
  heights.append(height)
  widths.append(width)


avg_height = sum(heights) / len(heights)
avg_width = sum(widths) / len(widths)

print('Average height: ' + str(avg_height))
print('Average width: ' + str(avg_width))


print('Max height: ' +str(max(heights)))
print('Max width: ' + str(max(widths)))

print('-----------------------------------------')

print(np.argmax(heights))
print(np.argmax(widths))





