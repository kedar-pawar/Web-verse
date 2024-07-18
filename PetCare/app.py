from flask import Flask, redirect,render_template,request, redirect, url_for, session
from flask_mysqldb import *
import os
import re
# from app import app
# import MySQLdb.cursors

app = Flask(__name__)
# Generate a secret key
app.secret_key = os.urandom(24)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'Pet_Care'
app.config['MYSQL_PASSWORD'] = '12345678'  # Make sure to use the correct password
app.config['MYSQL_DB'] = 'pet_CAre'

mysql = MySQL(app)
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/services')
def services():
    return render_template("services.html")

@app.route('/about')
def about():
    return render_template("aboutus.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/thank_you')
def feedback():
    return render_template("thank_you.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['txtName']
        email = request.form['txtEmail']
        message = request.form['txtMessage']

        # Insert the form data into the database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contact_us (name, email, message) VALUES (%s, %s, %s)", (name, email, message))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('feedback'))
    return render_template("contactus.html")

@app.route('/dogs')
def dogs():
    return render_template("services_dogs.html") 

@app.route('/cats')
def cats():
    return render_template("services_cats.html")

@app.route('/adoptdogs')
def adoptdogs():
    return render_template("dogs_adoption.html")

@app.route('/adoptcats')
def adoptcats():
    return render_template("cats_adoption.html")

@app.route('/pet_guardian')
def pet_guardian():
    return render_template("pet_guardian.html")



@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['txtName']
        email = request.form['txtEmail']
        password = request.form['txtpassword']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO User (name, email, password) VALUES (%s, %s, %s)", (name, email,password))
        mysql.connection.commit()
        cur.close()
        return render_template("login.html")
    # Add a return statement for the GET request case
    return render_template("register.html")


@app.route('/login', methods =['GET', 'POST'])
def login():
    mesage = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE email = % s AND password = % s', (email, password, ))
        user = cursor.fetchone()
        if user:
            session['loggedin'] = True
            #session['userid'] = user['userid']
            #session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('user.html', mesage = mesage)
        else:
            mesage = 'Please enter correct email / password !'
    return render_template('login.html', mesage = mesage)



@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('userid', None)
    session.pop('email', None)
    return redirect(url_for('login'))


@app.route('/adoption_process')
def adoption_process():
    return render_template('adoption_process.html')

@app.route('/submit_adoption', methods=['GET','POST'])
def submit_adoption():
    # Retrieve form data
    user_name = request.form['user_name']
    adopted_dog = request.form['adopted_dog']
    adopted_cat = request.form['adopted_cat']
    user_address = request.form['user_address']
    contact_number = request.form['contact_number']
    Email_ID= request.form['Email_ID']
    confirmation = request.form['confirmation']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Pet_Guardians (user_name,adopted_dog,adopted_cat,user_address,contact_number, Email_ID,confirmation) VALUES (%s, %s, %s,%s, %s, %s,%s)", (user_name,adopted_dog,adopted_cat,user_address,contact_number, Email_ID,confirmation))
    mysql.connection.commit()
    cur.close()
    # Here you would insert this data into the RDBMS table using SQL queries
    # For simplicity, I'll just print the data
    # Redirect to a thank you page or home page
    return redirect(url_for('confirmation'))

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')


# @app.route('/result')
# def result():
#     cur = mysql.connection.cursor()
#     cur.execute('select * from contact_us')
#     data = cur.fetchall()
#     cur.close()
#     return str(data)

if __name__ == '__main__':
    app.run(debug=True)

