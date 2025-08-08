# QR-tool

This project provides a local-only QR code cybersecurity awareness simulation.

## Features
- Flask web app that displays the visitor's IP address, browser user-agent, and timestamp.
- JavaScript alerts simulate a screenshot capture and request access to the camera.
- If camera access is denied, an alternate warning alert is shown.
- No data is stored or transmitted; information is displayed only during the session.
- `generate_qr.py` creates a QR code (`qr_code.png`) that links to `http://127.0.0.1:5000/`.

## Requirements
- Python 3
- Packages: Flask, qrcode[pil]

Install dependencies:
```bash
pip install Flask qrcode[pil]
```

## Running the Simulation
1. Generate the QR code:
   ```bash
   python generate_qr.py
   ```
   This produces `qr_code.png`.
2. Start the Flask application:
   ```bash
   python app.py
   ```
   The site is served at `http://127.0.0.1:5000/`.
3. Scan `qr_code.png` with a mobile device connected to the same machine. Adjust the URL in `generate_qr.py` to your network IP if you want other devices on the network to access the simulation.
4. Observe the displayed device information and alerts. Discuss with students what could happen on a real malicious site.

## Educational Notes
This simulation demonstrates risks of scanning untrusted QR codes:
- Attackers could log your IP, browser details, and visit time.
- Malicious pages might request camera or other sensitive permissions.
- Even simple alerts can be used to social-engineer users into granting access.

No information is stored or transmitted in this demo. Use it to promote safe QR code practices in a classroom setting.

## Disclaimer
This tool is for educational purposes only. It does not capture or transmit any real data.
