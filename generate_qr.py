import qrcode

URL = "http://127.0.0.1:5000/"

def main():
    img = qrcode.make(URL)
    img.save("qr_code.png")
    print("QR code saved as qr_code.png")

if __name__ == "__main__":
    main()
