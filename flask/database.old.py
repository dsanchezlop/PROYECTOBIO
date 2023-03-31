#Imports
from flask import Flask, render_template, request, redirect, session, url_for, flash
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
        if re.match("^[a-zA-ZÁáÉéÍíÓóÚúÜüñÑ]+(?:\s[a-zA-ZÁáÉéÍíÓóÚúÜüñÑ]+)*$", name):
        # Name contains only letters and spaces
            valid_name = True
        else:
            valid_name = False
        surname = bleach.clean(request.form['surname'])
        if re.match("^[a-zA-ZÁáÉéÍíÓóÚúÜüñÑ]+(?:\s[a-zA-ZÁáÉéÍíÓóÚúÜüñÑ]+)*$", surname):
        # Surname contains only letters and spaces
            valid_surname = True
        else:
            valid_surname = False
        password = bleach.clean(request.form['password'])
        confirm_password = bleach.clean(request.form['confirm-password'])
        if valid_name == True:
            if valid_surname == True:
                
                if password == confirm_password:
                    hashed_password = hashlib.sha256(password.encode()).hexdigest()
                    conn = mysql.connector.connect(**db_config)
                    cursor = conn.cursor()
                    try:
                        query3 = "INSERT INTO users (username, email, name, surname, passw, role) VALUES (%s, %s, %s, %s, %s, 2)"
                        cursor.execute(
                            query3, (username, email, name, surname, hashed_password))
                        conn.commit()
                        cursor.close()
                        conn.close()
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
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        print(hashed_password)
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT id ,username, passw, role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        print(result)
        cursor.close()
        conn.close()

        if result is not None and result[2] == hashed_password:
            session['user_id'] = result[0]
            session['username'] = username
            session['logged_in'] = True
            session['role'] = result[3]
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
    


def update_profile():
    if request.method == 'POST':
        # Retrieve form data
        username = bleach.clean(request.form['username'])
        name = bleach.clean(request.form['name'])
        surname = bleach.clean(request.form['surname'])
        email = bleach.clean(request.form['email'])
        password = bleach.clean(request.form['password'])
        confirmPassword = bleach.clean(request.form['confirmPassword'])
        
        # Validate form data
        if not username:
            flash('Name is required')
            return redirect(url_for('profile'))
        if not name:
            flash('Name is required')
            return redirect(url_for('profile'))
        if not surname:
            flash('Name is required')
            return redirect(url_for('profile'))
        if not email:
            flash('Email is required')
            return redirect(url_for('profile'))
        if password == confirmPassword:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Update user's profile information in the database
            user_id = session['user_id']
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            query = "UPDATE users SET username = %s ,name = %s, surname = %s, email = %s, passw = %s WHERE id = %s"
            cursor.execute(query, (username, name, surname, email, hashed_password, user_id))
            conn.commit()
            cursor.close()
            conn.close()  
        # Redirect back to the profile page
            flash('Profile updated')
            return redirect(url_for('profile'))
        else:
            return render_template('profile.html', error='Passwords do not match')
    else:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = "SELECT username, name, surname, email FROM users WHERE id = %s"
        cursor.execute(query, (session['user_id'],))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        return render_template('profile.html', user=user)
    

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
