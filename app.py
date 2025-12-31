import os
from flask import Flask, jsonify

app = Flask(__name__)

PORT = os.getenv("APP_PORT")

if not PORT:
    raise RuntimeError("APP_PORT environment variable is not set")

@app.route("/")
def home():
    return jsonify({
        "app": "Port Demo App",
        "port": PORT
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(PORT))

