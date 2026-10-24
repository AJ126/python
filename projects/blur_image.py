from PIL import Image, ImageFilter
img=Image.open("uploaded_files/Mahadev.jpg")
blur=img.filter(ImageFilter.GaussianBlur())
blur.show()