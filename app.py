from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, export_defaults=True, defaults_prefix='study_flask')
#Static metrics
metrics.info('app_info', 'Study of flask', version='0.0.3')


username = ''
email= '' 

# endpoints = ('/','/api')
# @app.route("/metrics")
# def metrics():
#     return metrics.app_info, 200

@app.route("/hello")
def hello():
    return "Hello World!", 200

# endpoint to create new user
@app.route("/api", methods=["GET"])
def get_user():    
    return jsonify(username,email), 200

@app.route("/api", methods=["POST"])
def add_user():    
    global username 
    global email

    username = request.json['username']

    if (username == ''):
        return 501, "invalid username"

    email = request.json['email']

    if (email == ''):
        return 501, "invalid username"
    
    return 'ok', 201


if __name__ == '__main__':    
    app.run('0.0.0.0', 5000
    )


