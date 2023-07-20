from flask import Flask, request, jsonify
# import os


app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))


users = []


@app.route('/')
def home():
    return 'Home'


@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "some@email.com"
    }
    """querry params 
    http://127.0.0.1:5000/get-user/1?extra="hellow"
    """
    extra = request.args.get('extra')
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200
    # http://127.0.0.1:5000/get-user/1


@app.route('/create-user', methods=["POST"])
def create_user():
    data = request.get_json()
    print(data)
    users.append(data)
    print(users)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True)
