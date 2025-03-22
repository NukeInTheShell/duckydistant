from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Dictionnaire pour stocker le dernier ping de chaque client
clients = {}

@app.route("/status", methods=["POST"])
def update_status():
    client_ip = request.remote_addr  # Récupère l'IP du client
    clients[client_ip] = time.time()  # Met à jour le timestamp
    return "", 200  # Réponse vide avec code 200 (OK)

@app.route("/connected_clients", methods=["GET"])
def get_connected_clients():
    current_time = time.time()
    active_clients = [
        ip for ip, last_seen in clients.items() if current_time - last_seen < 10
    ]  # Si un client a envoyé un ping il y a moins de 10 sec, il est en ligne
    return jsonify({"connected_clients": active_clients})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
