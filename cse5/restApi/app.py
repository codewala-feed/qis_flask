from flask import Flask, request

app = Flask(__name__)

details = {}

@app.route("/fetch/<int:user_id>", methods=["GET"])
def get_data(user_id):
    user = details.get(user_id)
    if user is not None:
        return {"response":user}, 200
    else:
       return {"response":"User Not Found :("}, 404 

@app.route("/create", methods=["POST"])
def create_data():
    raw = request.json
    key = raw.get("user_id")
    value = raw.get("data")
    if (key is not None) and (value is not None):
        details[key] = value
        return {"response":"User Created :)"}, 201
    else:
        return {"response":"Invalid Data"}, 404


@app.route("/update", methods=["PUT"])
def update_data():
    raw = request.json
    key = raw.get("user_id")
    value = raw.get("data")
    if key in details:
        details[key] = value
        return {"response":"user updated "}, 200
    else:
        return {"response":"User Not Found"}, 404


@app.route("/delete", methods=["DELETE"])
def delete_data():
    raw = request.json
    key = raw.get("user_id")
    if key in details:
        details.pop(key)
        return {"response":"User Deleted :("}, 200
    else:
        return {"response":"User Not Found"}, 404