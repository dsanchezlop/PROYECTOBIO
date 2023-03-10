mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register_post():
    username = request.form.get('username')
    password = request.form.get('password')
    # Insert user into the database
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    return "User created!"

if __name__ == '__main__':
    app.run(debug=True)








.container {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    font-size: 2em;
    margin-bottom: 20px;
    
}

.form-group {
    margin-bottom: 20px;
    max-width: 500px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-size: 1.2em;
    font-weight: bold;
}

input[type="text"],
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 10px;
    font-size: 1.2em;
    border: 2px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
}

input[type="submit"] {
    background-color: #007bff;
    color: #fff;
    padding: 10px;
    font-size: 1.2em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.2s ease-in-out;
}

input[type="submit"]:hover {
    background-color: #0062cc;
}

.error-message {
    color: red;
    font-size: 1.1em;
    margin-top: 10px;
}

/* Media queries */
@media screen and (max-width: 600px) {
    .container {
        max-width: 100%;
        padding: 10px;
    }
}