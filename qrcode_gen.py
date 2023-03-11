#import qrcode
#qr = qrcode.QRCode(
#    version=4,
#    error_correction=qrcode.constants.ERROR_CORRECT_L,
#    box_size=15,
#    border=4,
#)
#qr.add_data('https://www.nexevo.in/')
#qr.make(fit=True)

#img = qr.make_image(fill_color="black", back_color="white")
#img.save("nexevo.jpg")


import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('Some data')

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="E:/Maran/Sample_Py/SamplePy/nexevo.jpg")

