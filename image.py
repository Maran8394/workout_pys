from PIL import Image
from io import BytesIO
output = BytesIO()

img  = Image.open(r"C:\Users\Bala\Pictures\nature.jpg")
w,h = img.size
new_size = (200,200)
img1 = img.resize(new_size)
img1.save(output,'PNG')
img1.show()
size = output.tell()
print("{:.2f} KB".format(size/1e+6))
