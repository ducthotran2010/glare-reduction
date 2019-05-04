import cv2
import numpy
from constant import *


# ========================================
# Show case
for image_name in original_image_name_list:
    print("Image:", image_name)
    local_name_ori = original_dir + '/' + image_name
    local_name_1st = first_method_dir + '/' + image_name
    local_name_3rd = third_method_dir + '/' + image_name

    ori_img = cv2.imread(local_name_ori)
    first_img = cv2.imread(local_name_1st)
    third_img = cv2.imread(local_name_3rd)

    ori_img = cv2.resize(ori_img, (0,0), fx=0.5, fy=0.5)
    first_img = cv2.resize(first_img, (0,0), fx=0.5, fy=0.5)
    third_img = cv2.resize(third_img, (0,0), fx=0.5, fy=0.5)

    cv2.putText(first_img, "RG", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 255), 3)
    cv2.putText(third_img, "RG + EC", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2.5, (0, 0, 255), 3)

    cv2.imshow('SHOWCASE', numpy.hstack([ori_img, first_img, third_img]))

    cv2.waitKey(0)
    
cv2.destroyAllWindows()
# ========================================