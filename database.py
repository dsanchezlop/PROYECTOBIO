from flask import Flask, render_template, request, redirect, session, url_for

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



def registration():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        name = request.form['name']
        surname = request.form['surname']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        if password == confirm_password:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            try:
                query3 = "INSERT INTO users (username, email, name, surname, passw, role) VALUES (%s, %s, %s, %s, %s, 2)"
                cursor.execute(
                    query3, (username, email, name, surname, password))
                conn.commit()
                cursor.close()
                conn.close()
                session['username'] = username
                return redirect('/login')
            except mysql.connector.Error as error:
                print(f"Error while executing SQL query: {error}")
                return render_template('register.html', error='Username or email not valid')
        else:
            return render_template('register.html', error='Passwords do not match')
    else:
        return render_template('register.html')
    

def log_in():
    print(request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT username, passw, role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result is not None and result[1] == password:
            session['username'] = username
            session['logged_in'] = True
            session['role'] = result[2]
            print (result[2])
            print (session['role'])
            return redirect('/')
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')


def log_out():
    session.pop('username', None)
    session['logged_in'] = False
    return redirect('/')
    

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
