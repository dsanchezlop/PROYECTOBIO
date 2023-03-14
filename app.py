from flask import Flask, render_template, request, redirect, session, url_for
import database



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
    if 'username' not in session: 
        result = database.registration()
        return result
    else:
        return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' not in session:
        result = database.log_in()
        return result
    else:
        return redirect('/')

@app.route('/logout', methods=['GET'])
def logout():
    if 'username' in session:
        result = database.log_out()
        return result
    else:
        return redirect('/')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect('/')
    else:
        return render_template('profile.html')

@app.route('/database', methods=['GET', 'POST'])
def data_base():
    return render_template('database.html')

@app.route('/maps', methods=['GET', 'POST'])
def maps():
    return render_template('maps.html')

@app.route('/fauna_maps', methods=['GET', 'POST'])
def fauna_maps():
    return render_template('fauna_maps.html')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')

if __name__ == '__main__':

    app.run(debug=True)
