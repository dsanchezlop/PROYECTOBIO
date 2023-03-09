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