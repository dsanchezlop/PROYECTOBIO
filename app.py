from flask import Flask, render_template
import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/acerca-de')
# def acerca_de():
#     return render_template('acerca_de.html')

# @app.route('/contacto')
# def contacto():
#     return render_template('contacto.html')

if __name__ == '__main__':
    
    app.run(debug=True)