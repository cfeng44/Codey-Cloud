from flask import jsonify

def json_response(data, status=200):
    return jsonify({"data": data, "status": status})

def add_routes(app):
    @app.route("/")
    def home():
        return json_response("Hello, World!")

    @app.route("/ping")
    def ping():
        return json_response("Pong!")
