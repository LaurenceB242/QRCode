import qrcode

data = "https://example.com"
img = qrcode.make(data)
img.save("mon_qr_code.png")
print("QR code généré avec succès !")