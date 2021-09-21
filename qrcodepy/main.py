import qrcode
import image

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

value = "https://github.com/sasankaweera123"

qr.add_data(value)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")