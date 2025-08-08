# QR-tool

## Req
- Python 3
- Packages: Flask, qrcode[pil]

install it:
```bash
pip install Flask qrcode[pil]
```

## how it is 
1. Generate the QR:
   ```bash
   python generate_qr.py
   ```
   generated qr `qr_code.png`.
2. Start the Flask appli:
   ```bash
   python app.py
   ```
   site is served at `http://127.0.0.1:5000/`.
3. Scan `qr_code.png` with a mobile device connected to the same machine. Adjust the URL in `generate_qr.py` to your network IP ```if you want other devices on the network to access the simulation.```

## Disclaimer
remember it is only for educational purposes only. It does not capture or transmit any real 🤐😛
