from flask import Flask, jsonify

app = Flask(__name__)
app.json.sort_keys = False


@app.route("/api/health", methods=["GET"])
def health_check():
    """Report that the API process is up."""
    return jsonify({"status": "healthy", "service": "weather-service"})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
