import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

print("Enter the text to be encoded in the QR code:")
text = input()

qr.add_data(text)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
sava_as = input("the qr code file to be saved as: ")
# the_file =(sava_as.append(".png"))

print("the qr code is saved as: {}.png".format(the_file))
img.save(the_file)