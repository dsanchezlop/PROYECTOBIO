#Imports
from flask import Flask, render_template, request, redirect, session, url_for
import mysql.connector
import bleach
import hashlib
import re

app = Flask(__name__)
app.secret_key = ''

#Configuration parameter for access to the database
db_config = {
    'host': 'localhost',
    'user': 'adminProject',
    'password': 'admin',
    'database': 'proyecto-bio'
}


#Registration to the webpage:
#   if the method is POST:
#       if successful: 
#           user is added to the database and redirected to the login
#       else:
#           renders the registration template with an error message
#   else:
#       return redirection to the register.html template 
def registration():
    if request.method == 'POST':
        valid_name = False
        valid_surname = False

        username = bleach.clean(request.form['username'])
        email = bleach.clean(request.form['email'])
        name = bleach.clean(request.form['name'])
        if re.match("^[A-Za-z ]*$", name):
        # Name contains only letters and spaces
            valid_name = True
        else:
            valid_name = False
        surname = bleach.clean(request.form['surname'])
        if re.match("^[A-Za-z ]*$", surname):
        # Surname contains only letters and spaces
            valid_surname = True
        else:
            valid_surname = False
        password = bleach.clean(request.form['password'])
        confirm_password = bleach.clean(request.form['confirm-password'])
        if valid_name == True:
            if valid_surname == True:
                
                if password == confirm_password:
                    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    try:
                        query3 = "INSERT INTO users (username, email, name, surname, passw, role) VALUES (%s, %s, %s, %s, %s, 2)"
                        cursor.execute(
                            query3, (username, email, name, surname, hashed_password))
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
                return render_template('register.html', error='Surname is not valid')
        else:
            return render_template('register.html', error='Name is not valid')
    else:
        return render_template('register.html')


#Log in to the webpage:
#   if the method is POST:
#       if successful: 
#           return user logged in and a session is created with the username, role and if it's logged 
#       else:
#           returns render the login template with an error message
#   else:
#       return render the login template
def log_in():
    if request.method == 'POST':
        username = bleach.clean(request.form['username'])
        password = bleach.clean(request.form['password'])
        hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(hashed_password)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT username, passw, role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()

        if result is not None and result[1] == hashed_password:
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


#Log out of the webpage:
#   Logs out of the webapge
def log_out():
    session.pop('username', None)
    session.pop('role', None)
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
