from flask import Flask, request, jsonify

app = Flask(__name__)
username = ''
email= '' 
@app.route("/")
def hello():
    return "Hello World!"

# endpoint to create new user
@app.route("/api", methods=["GET"])
def get_user():    
    return jsonify(username,email)

@app.route("/api", methods=["POST"])
def add_user():    
    global username 
    global email

    username = request.json['username']
    email = request.json['email']
    
    return jsonify(username,email)


if __name__ == '__main__':    
    app.run(debug=True,host= '0.0.0.0')


