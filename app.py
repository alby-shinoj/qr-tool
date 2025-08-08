from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>QR Code Security Simulation</title>
  <script>
    window.onload = function() {
      alert("This site could have attempted to capture a screenshot!");
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true })
          .then(function(stream) {
            stream.getTracks().forEach(track => track.stop());
            alert("Camera access granted (simulation only, nothing recorded).");
          })
          .catch(function(err) {
            alert("Camera access denied. In a real attack, a site could keep trying or misuse your camera.");
          });
      } else {
        alert("Camera API not supported in this browser.");
      }
    };
  </script>
  <style>
    body { font-family: Arial, sans-serif; margin: 2em; }
    .log { background: #f0f0f0; padding: 1em; margin-bottom: 1em; }
    .warning { color: #b30000; }
  </style>
</head>
<body>
  <h1>QR Code Cybersecurity Awareness Simulation</h1>
  <div class="log">
    <p><strong>Visitor IP:</strong> {{ ip }}</p>
    <p><strong>User Agent:</strong> {{ ua }}</p>
    <p><strong>Timestamp:</strong> {{ ts }}</p>
  </div>
  <p class="warning">If this were a malicious site, it could capture your device details, take screenshots, or access your camera without permission.</p>
  <p>This simulation does <em>not</em> store or transmit any data and is safe for educational use.</p>
</body>
</html>
"""


@app.route("/")
def index():
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(TEMPLATE, ip=ip, ua=ua, ts=ts)


if __name__ == "__main__":
    app.run(debug=True)
