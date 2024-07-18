from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['UPLOAD_FOLDER'] = 'D:/project/templates/uploads'  
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "Kedar"
app.config["MYSQL_PASSWORD"] = "1234567"
app.config["MYSQL_DB"] = "Vital_care"

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('intro_page'))  # Redirect to /intro_page

@app.route('/intro.html')
def intro_page():
    return render_template('intro.html')

@app.route('/templates/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/index2.html')
def login():
    return render_template('index2.html')

@app.route('/process_login', methods=['POST'])
def process_login():
    pat_id = request.form.get('Pat_ID')
    pat_name = request.form.get('Pat_name')

    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Patient WHERE Pat_ID = %s", (pat_id,))
        patient_data = cur.fetchone()
        cur.close()

        if patient_data:
            # Patient found, render the patient details template
            return render_template('sample.html', patient=patient_data)
        else:
            # Patient not found, render an error message or redirect to login
            return render_template('msg2.html', error="Patient not found")

    except Exception as e:
        return f"Error processing login: {str(e)}"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        Pat_name = request.form['name']
        Pat_Phone_number = request.form['mobile_no']
        Pat_Address = request.form['address']
        Pat_Gmail_ID = request.form['Gmail']
        Pat_Blood_Group = request.form['dropdown']
        Pat_Symptoms = request.form['symptoms']
        Pat_Date_of_birth = request.form['date_of_birth']
        Pat_city = request.form['city']
        Pat_State = request.form['state']
        Pat_Nationality = request.form['nationality']
        Pat_IMG = request.files['image']

        # Handle photo upload
        if 'image' in request.files:
            Pat_IMG= request.files['image']
            # Save the photo to the 'uploads' folder
            if not os.path.exists('uploads'):
                os.makedirs('uploads')
            Pat_IMG.save('uploads/' + Pat_IMG.filename)

        try:
            # Insert data into the database
            cur = mysql.connection.cursor()
            cur.execute("""
                        INSERT INTO Patient (
                            Pat_name, Pat_Phone_number, Pat_address, Pat_Gmail_ID, Pat_Blood_Group, 
                            Pat_Symptoms, Pat_Date_of_birth, Pat_city, Pat_State, Pat_Nationality, 
                            Pat_image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                            """, (
                                Pat_name, Pat_Phone_number, Pat_Address, Pat_Gmail_ID, Pat_Blood_Group,
                                Pat_Symptoms, Pat_Date_of_birth, Pat_city, Pat_State, Pat_Nationality,
                                'uploads/' + Pat_IMG.filename if 'image' in request.files else None
                            ))
            mysql.connection.commit()
            cur.close()

            # Redirect to the login page
            return redirect(url_for('login'))
        except Exception as e:
            return f"Error inserting data: {str(e)}"

    # Render the signup form page for GET requests
    return render_template('background.html')

@app.route('/appointment/<int:App_id>')
def appointment(App_id):
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM Appointment WHERE App_id = %s", (App_id,))
        appointment_data = cur.fetchone()
        cur.close()

        if appointment_data:
            return render_template('appointment.html', appointment=appointment_data)
        else:
            return render_template('msg2.html', error="Appointment not found")

    except Exception as e:
        return f"Error processing appointment data: {str(e)}"
    


@app.route('/templates/app_log.html')
def app_log():
    return render_template('app_log.html')


@app.route('/App_process_login', methods=['POST'])
def App_process_login():
    app_id = request.form.get('app_id')
    pat_id = request.form.get('pat_id')

    try:
        with mysql.connection.cursor() as cur:
            cur.execute("SELECT * FROM Appointment WHERE App_id = %s", (app_id,))
            appointment_data = cur.fetchone()

        if appointment_data:
            # Patient found, render the patient details template
            return render_template('sample1.html', appointment=appointment_data)
        else:
            # Patient not found, render an error message or redirect to login
            return render_template('msg2.html', error="Patient not found")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return render_template('error.html', error="An unexpected error occurred.")

@app.route('/after_login')
def after_login():
    return render_template('sample1.html')

@app.route('/templates/paper.html')
def paper():
    return render_template('paper.html')

if __name__ == "__main__":
    app.run(debug=True, port=5501)