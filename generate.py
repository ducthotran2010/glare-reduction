import cv2
import glob
import numpy
from helper import *
from constant import *


# ========================================
# Load data from Original directory
print("Loading data...")

original_image_list = []
for file_name in glob.glob(original_dir + '/*.jpg'):
    image = cv2.imread(file_name)
    original_image_list.append(image)

print("Done")
# ========================================



# ========================================
# Create directories
try:
    os.mkdir(generated_image_dir)
    "generated_image_dir created"
except FileExistsError:
    "generated_image_dir already exists"

for image_dir in preprocess_image_dir:
    try:
        os.mkdir(generated_image_dir + '/' + image_dir)
        "image_dir created"
    except FileExistsError:
        "image_dir already exists"
# ========================================



# ========================================
# First processing method: Reduce glare (RG)
print("\nExecuting first method: Reduce glare (RG)...")

for image, image_name in zip(original_image_list, original_image_name_list):
    _image = reduce_glare(image)
    local_name = first_method_dir + '/' + image_name
    cv2.imwrite(local_name, _image)

print("Executed")
# ========================================



# ========================================
# Third processing method: Reduce glare + Enhance contrast (RG + EC)
print("\nExecuting third method: Reduce glare + Enhance contrast (RG + EC)...")

for image, image_name in zip(original_image_list, original_image_name_list):
    _image = mix_filter(image)
    local_name = third_method_dir + '/' + image_name
    cv2.imwrite(local_name, _image)
print("Executed")
# ========================================

print("\nPre-processing image is done. Run show_case.py to get detail.")
