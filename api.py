from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/savin", methods=["POST"])
def savin():
    data = request.json
    command = data.get("command", "")
    print("Received command:", command)
    return jsonify({"message": f"Executing {command}...", "status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
