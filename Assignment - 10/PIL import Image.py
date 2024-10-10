from PIL import Image

image = Image.open("example.jpg")

crop_area = (100, 100, 400, 400)  

cropped_image = image.crop(crop_area)

cropped_image.save("cropped_example.jpg")

print("Image cropped and saved as 'cropped_example.jpg'.")