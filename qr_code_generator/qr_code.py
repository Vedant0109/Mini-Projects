import qrcode

input= "www.https://github.com/Vedant0109"

qr= qrcode.make(input)

qr.save("test_qr.png")