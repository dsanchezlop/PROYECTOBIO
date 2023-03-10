from flask import Flask, render_template, redirect, url_for
import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    
@app.route('/redirect-to-login')
def redirect_to_login():
    return redirect(url_for('login'))

@app.route('/register')
def register():
    return render_template('register.html')
    
@app.route('/redirect-to-register')
def redirect_to_register():
    return redirect(url_for('register'))

if __name__ == '__main__':
    
    app.run(debug=True)