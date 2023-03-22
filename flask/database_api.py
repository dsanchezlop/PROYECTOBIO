import hashlib
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://<username>:<password>@<host>/<database>'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50),  nullable=False)
    email = db.Column(db.String(50), nullable=False)
    role = db.Column(db.Integer, nullable=False)

    def __init__(self, username, password, name, surname, email, role):
        self.username = username
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        self.name = name
        self.surname = surname
        self.email = email
        self.role = role

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and user.password == hashlib.sha256(password.encode('utf-8')).hexdigest():
        return jsonify({'success': True}), 200
    else:
        return jsonify({'success': False}), 401


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'})


@app.route('/register', methods=['POST'])
def register():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    surname = request.json['surname']
    email = request.json['email']
    role = 'registered'

    if not username or not email or not password or not name or not surname or not email:
        return jsonify({'message': 'Missing parameters'}), 400
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({'message': 'Username already taken'}), 409
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'Email already registered'}), 409
    user = User(username, password, name, surname, email, password, role)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'Registration successful'}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    if username:
        user.username = username
    if email:
        user.email = email
    if password:
        user.set_password(password)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True)
