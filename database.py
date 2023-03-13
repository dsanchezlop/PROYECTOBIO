from flask import Flask, render_template, request, redirect, session
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'key'

db_config = {
    'host': 'localhost',
    'user': 'adminProject',
    'password': 'admin',
    'database': 'proyecto-bio'
}

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

#         conn = mysql.connector.connect(**db_config)
#         cursor = conn.cursor()
#         query = "INSERT INTO users (email, password) VALUES (%s, %s)"
#         cursor.execute(query, (email, hashed_password))
#         conn.commit()
#         cursor.close()
#         conn.close()

#         session['email'] = email
#         return redirect('/dashboard')
#     else:
#         return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT username, password FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result is not None and result[1] == hashed_password:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
