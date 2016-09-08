#-*- coding: utf-8
# Add a number on the right corner of a picture
from PIL import Image, ImageDraw, ImageFont  # Python Imaging Library


def addNum( img ):
	size = img.size
	numSize = int( size[0] / 8 )
	font = ImageFont.truetype('arial', numSize )
	img = img.resize((size[0]-numSize * 2, size[1]-numSize * 2))
	newImg = Image.new('RGB', size, 'WHITE')
	newImg.paste(img, (numSize, numSize))
	draw = ImageDraw.Draw(newImg)
	#draw.text((size[0]-numSize, 0), '5', font=font, fill='RED')
	draw.ellipse((size[0]-numSize * 2, int(numSize / 2), size[0]-int(numSize / 2), numSize * 2), fill='RED', outline='RED')
	#newImg.show()
	newImg.save('new.png', 'png')
	#print(img.histogram())


if __name__ == "__main__":
	PicPath = "TestPic.jpg"
	img = Image.open(PicPath)
	print(img, img.size)
	addNum( img )
	#img.show()

