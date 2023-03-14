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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
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
                # query = "SELECT username FROM users WHERE username = %s"
                # cursor.execute(query, (username,))
                # result = cursor.fetchone()
                # cursor.close()
                # conn.close()
                # if result is not None:
                #     return render_template('register.html', error='Invalid username')
                # else:
                #     query2 = "SELECT email FROM users WHERE email = %s"
                #     cursor.execute(query2, (email,))
                #     conn.commit()
                #     result2 = cursor.fetchone()
                #     cursor.close()
                #     conn.close()
                #     if result2 is not None:
                #         return render_template('register.html', error='Invalid email')
                #     else:
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    print(request.method)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT username, passw FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        if result is not None and result[1] == password:
            session['username'] = username
            return redirect('/')
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


@app.route('/redirect-to-login')
def redirect_to_login():
    return redirect(url_for('login'))


@app.route('/redirect-to-register')
def redirect_to_register():
    return redirect(url_for('register'))


if __name__ == '__main__':

    app.run(debug=True)
