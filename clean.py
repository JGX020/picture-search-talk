import ImageEnhance,Image

image=Image.open('11.jpg')
def main(image):
	#size=width,height=image.size
    enhancer = ImageEnhance.Sharpness(image)
    image=enhancer.enhance(2.0)
if __name__ == "__main__":
	 main(image)
	 image.save("modified_11.jpg")
#for i in range(8):
 #   factor = i / 4.0
  #  enhancer.enhance(factor).show("Sharpness %f" % factor)