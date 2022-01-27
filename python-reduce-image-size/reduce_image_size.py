import os, sys
from PIL import Image
 
orig_img_dir = "original_images/"
dirs = os.listdir(orig_img_dir)
 
print('Image Size Reduction Started...')
 
for img in dirs:
    if os.path.isfile(orig_img_dir + img):
        im = Image.open(orig_img_dir + img)
        img_name = os.path.basename(orig_img_dir + img)
        width, height = im.size       
        im = im.resize((width, height), Image.ANTIALIAS)
        im.save('scaled_images/' + img_name)
        #im.save('optimized_images/' + img_name, optimize=True, quality=95)
        im.save('optimized_images/' + img_name, optimize=True, quality=85)
 
print('Image Size Reduction Done.')