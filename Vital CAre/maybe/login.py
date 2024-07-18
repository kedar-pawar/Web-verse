from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "Kedar"
app.config["MYSQL_PASSWORD"] = "1234567"
app.config["MYSQL_DB"] = "Vital_care"

mysql = MySQL(app)


@app.route('/')
def index():
    return redirect(url_for('login'))  # Redirect to /index2.html


@app.route('/index2.html')
def login():
    return render_template('index2.html')


@app.route('/process_login', methods=['GET'])
def process_login():
    pat_id = request.args.get('Pat_ID')
    pat_name = request.args.get('Patname')

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Patient WHERE Pat_ID = %s", (pat_id,))
        patient_data = cur.fetchone()
        cur.close()

        if patient_data:
            # Patient found, render the patient details template
            return render_template('patient_details.html', patient=patient_data)
        else:
            # Patient not found, render an error message or redirect to login
            return render_template('login.html', error="Patient not found")

    except Exception as e:
        return f"Error processing login: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)
