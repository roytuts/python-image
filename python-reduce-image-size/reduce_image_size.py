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
        
        # Resize the image
        new_width = int(width / 2)
        new_height = int(height / 2)
        resized_img = im.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save('scaled_images/' + img_name)
        
        # Compress the image
        im.save('optimized_images/' + img_name, quality=85, optimize=True)
        
        # Convert to WEBP
        img_name_without_extension = os.path.splitext(os.path.basename(img_name))[0]
        im.save('webp_images/' + img_name_without_extension + '.webp', format="WEBP")

print('Image Size Reduction Done.')
