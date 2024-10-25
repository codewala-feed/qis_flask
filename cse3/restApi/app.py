from flask import Flask, request

app = Flask(__name__)

details = {}

@app.route("/fetch/<int:user_id>", methods=["GET"])
def get_data(user_id):
    user = details.get(user_id)
    if user is not None:
        return {"response": user}, 200
    else:
        return {"response":"No User Found :("}, 404

@app.route("/create", methods=["POST"])
def create_data():
    raw = request.json
    key = raw.get("user_id") #1000
    value = raw.get("data") #{"name":"stefan", "age":23}
    details[key] = value
    return {"response":"data received"}, 201