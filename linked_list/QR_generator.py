import qrcode

# QR code data
data = "https://chat.whatsapp.com/GHIZe9u50I90lNKpBi0zNJ"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save("tarih_kulübüwp.png")