from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] ='K:\projectK\projectK\project\templates'
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "Kedar"
app.config["MYSQL_PASSWORD"] = "1234567"
app.config["MYSQL_DB"] = "Vital_care"

mysql = MySQL(app)

@app.route('/')
def index():
   return render_template('templates/direct_appointment.html')  # Redirect to /intro_page

# Define the route for the direct appointment page access
@app.route('/direct_appointment', methods=['GET', 'POST'])
def direct_appointment():
    if request.method == 'POST':
        app_id = request.form['app_id']
        pat_id = request.form['pat_id']

        # Validate the App_id and Pat_id against the database
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Appointment WHERE App_id = %s AND Pat_id = %s", (app_id, pat_id))
        if appointment:
            # Redirect to the appointment page with the validated App_id and Pat_id
            return redirect(url_for('appointment1', app_id=app_id, pat_id=pat_id))
        else:
            # Handle invalid input, you can customize 
            # this part
            return render_template('invalid_input.html')

    return render_template('direct_appointment.html')

@app.route('/appointment1/<int:App_id>/<int:Pat_id>')
def appointment1(App_id, Pat_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Appointment WHERE App_id = %s AND Pat_id = %s", (App_id, Pat_id))
        appointment_data = cur.fetchone()
        cur.close()

        if appointment_data:
            return render_template('appointment1.html', appointment=appointment_data)
        else:
            return render_template('msg2.html', error="Appointment not found")

    except Exception as e:
        return f"Error processing appointment data: {str(e)}"

@app.route('/appointment/paper.html')
def paper():
    return render_template('paper.html')

if __name__ == "__main__":
    app.run(debug=True)
