import os 
import glob

original_dir = 'Test_Original'

generated_image_dir = 'Generated_Image'

original_image_name_list = [os.path.basename(img_name) for img_name in glob.glob(original_dir + '/*.jpg')]

preprocess_image_dir = [
    '001',
    '003',
]


first_method_dir = generated_image_dir + '/' + preprocess_image_dir[0]
third_method_dir = generated_image_dir + '/' + preprocess_image_dir[1]

