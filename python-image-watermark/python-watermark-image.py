import os, sys
from PIL import Image, ImageDraw, ImageFont

img_dir = "images/non-watermark/"
dirs = os.listdir( img_dir )

for img in dirs:
	if os.path.isfile(img_dir + img):
		#Create an Image Object from an Image
		im = Image.open(img_dir + img)
		
		#Image width and height
		width, height = im.size
		
		#Image name
		img_name = os.path.basename(img_dir + img)
		
		#print(img_name)

		text = "{roytuts.com}"
		font = ImageFont.truetype('arial.ttf', 30)
		
		draw = ImageDraw.Draw(im)
		
		textwidth, textheight = draw.textsize(text, font)

		#Right bottom corner with margin 5 from right
		margin = 5
		#x = width - textwidth - margin
		#y = height - textheight - margin
		
		#Center of the image
		x = (width - textwidth)/2 #center
		y = (height - textheight)/2 #center
		
		#draw.text((x, y), text, font=font)
		draw.text((x, y), text, font=font, fill=(254, 130, 75, 15))
		#im.show() //Will display in the image window
		
		#Save watermarked image
		im.save('images/watermark/' + img_name)