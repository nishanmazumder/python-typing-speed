import qrcode as qr
from PIL import Image

# Package https://github.com/lincolnloop/python-qrcode.git

# img = qr.make('https://github.com/lincolnloop/python-qrcode.git')
# img.save('qrcode.png')

# print(type(img))

code = qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

code.add_data("Product Code!")
code.make(fit=True)
img = code.make_image(fill_color='blue', back_color='white')
img.save('qr.png')
