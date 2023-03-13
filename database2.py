from flask import Flask, render_template, request, session, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector
import hashlib

app = Flask(__name__)
app.secret_key = 'secret_key'

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'adminProject'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'proyecto-bio'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Retrieve form data
        username = request.form['username']
        password = request.form['password']

        # Check if user exists in the database
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()

        if user:
            # Check if password matches
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            if hashed_password == user[2]:
                # Log in the user and create a session
                session['logged_in'] = True
                session['username'] = user[1]
                return redirect(url_for('dashboard'))
            else:
                # Incorrect password
                error = 'Incorrect password'
        else:
            # User not found
            error = 'Username not found'

    return render_template('login.html', error=error if 'error' in locals() else None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Retrieve form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash the password using SHA256
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

        # Insert the user into the database
        cursor = mysql.connection.cursor()
        cursor.execute('INSERT INTO users(username, email, passw) VALUES(%s, %s, %s)', (username, email, hashed_password))
        mysql.connection.commit()
        cursor.close()

        # Log in the user and create a session
        session['logged_in'] = True
        session['username'] = username

        # Redirect to the dashboard
        return redirect(url_for('dashboard'))

    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)

