#Imports
from flask import Flask, render_template, request, redirect, session, url_for
import database

app = Flask(__name__)
app.secret_key = 'key'

#Checks if there is a role assigned to the session
@app.before_request
def before_request():
    if 'role' not in session:
        session['role'] = 0

# Route for home
@app.route('/')
def home():
    before_request()
    return render_template('home.html')

# If username not in session:
#   do the database.registration
# Else:
#   redirects to home
@app.route('/register', methods=['GET', 'POST'])
def register():
    before_request()

    if 'username' not in session: 
        result = database.registration()
        return result
    else:
        return redirect('/')

# If:username not in session:
#   route for login
# Else:
#   redirects to home
@app.route('/login', methods=['GET', 'POST'])
def login():
    before_request()
    if 'username' not in session:
        result = database.log_in()
        return result
    else:
        return redirect('/')

# If username in session:
#   route to logout
# Else: 
#   redirects to home
@app.route('/logout', methods=['GET'])
def logout():
    before_request()
    if 'username' in session:
        result = database.log_out()
        return result
    else:
        return redirect('/')

# If username not in session:
#   redirects to home
# Else:
#   route to profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    before_request()
    if 'username' not in session:
        return redirect('/')
    else:
       result = database.update_profile()
       return result

# Route for database
@app.route('/database', methods=['GET', 'POST'])
def data_base():
    before_request()
    print(session['role'])
    return render_template('database.html')

# Route for maps
@app.route('/maps', methods=['GET', 'POST'])
def maps():
    before_request()
    print(session['role'])
    return render_template('maps.html')

# Route for fauna maps
@app.route('/fauna_maps', methods=['GET', 'POST'])
def fauna_maps():
    before_request()
    print(session['role'])
    return render_template('fauna_maps.html')

# If username in session route for dashboard
# else redirects to login
@app.route('/dashboard')
def dashboard():
    before_request()
    print(session['role'])
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

# If page not found route to home
@app.errorhandler(404)
def page_not_found(e):
    before_request()
    print(session['role'])
    return redirect('/')

if __name__ == '__main__':

    app.run(debug=True)
