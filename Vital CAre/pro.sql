create database Vital_care;
use Vital_care;
drop database Vital_care;
truncate patient;
CREATE TABLE Patient (
    Pat_id INT PRIMARY KEY AUTO_INCREMENT,
    Pat_name VARCHAR(50) NOT NULL,
    Pat_Phone_number BIGINT,
    Pat_address VARCHAR(50),
    Pat_Gmail_ID VARCHAR(50),
    Pat_Blood_Group VARCHAR(5),
    Pat_Symptoms VARCHAR(50),
    Pat_Date_of_birth VARCHAR(25) NOT NULL,
    Pat_city VARCHAR(50),
    Pat_State VARCHAR(50),
    Pat_Nationality VARCHAR(50),
    Pat_image BLOB,
	Pat_photo_path VARCHAR(255),  
    INDEX idx_Pat_id (Pat_id)
);

#INSERT INTO Patient (Pat_name, Pat_last, Pat_Phone_number, Pat_Gmail_ID, Pat_Blood_Group, Pat_Symptoms, Pat_Date_of_birth)
#VALUES ('John', 'Doe', 1234567890, 'john.doe@example.com', 'A', 'Fever', '1990-01-01');
select * from patient;

CREATE TABLE Doctor (
    Doc_id INT PRIMARY KEY AUTO_INCREMENT,
    Doc_name VARCHAR(50) NOT NULL,
    Doc_Phone_number BIGINT,
    Doc_Gmail_ID VARCHAR(50),
    Doc_Blood_Group VARCHAR(5),
    Doc_Specalist VARCHAR(50),
    Doc_Date_of_birth VARCHAR(25) NOT NULL,
    DOC_image BLOB,
   DOC_photo_path VARCHAR(255),  #-- Store the path to the doctor's photo
    INDEX idx_Doc_id (Doc_id)
);

#INSERT INTO Doctor (Doc_First_name, Doc_last_name, Doc_Phone_number, Doc_Gmail_ID, Doc_Blood_Group, Doc_Specalist, Doc_Date_of_birth)
#VALUES ('Jane', 'Smith', 9876543210, 'jane.smith@example.com', 'B', 'Cardiologist', '1985-05-15');
INSERT INTO DOCTOR (Doc_name, Doc_Phone_number, Doc_Gmail_ID, Doc_Blood_Group, Doc_Specalist, Doc_Date_of_birth, DOC_image, DOC_photo_path)
VALUES 
    ("Dr. Sangram Patil", 9192345687, "Stp@gmail.com", "A+", "Anesthesiology", "1980-09-24", NULL, 'C:/Users/dell/Desktop/painting-cute-naruto-605pg7cqdnzhthjx.webp'),
    ("Dr. Aishwarya Pawar", 7182381913, "alp@gmail.com", "A+", "Dentist", "2000-11-29", NULL, 'C:/Users/dell/Desktop/painting-cute-naruto-605pg7cqdnzhthjx.webp'),
    ("Dr. Nitya Sharma", 8765493673, "ns@gmail.com", "B", "Cardiologist", "1990-12-03", NULL, 'C:/Users/dell/Desktop/painting-cute-naruto-605pg7cqdnzhthjx.webp'),
    ("Dr. Aamit Shah", 9786534620, "as@gmail.com", "B+", "Neurologist", "1978-04-23", NULL, 'C:/Users/dell/Desktop/painting-cute-naruto-605pg7cqdnzhthjx.webp'),
    ("Dr. Shivay Oberoy", 8795698674, "so@gmail.com", "O", "Gynecologist", "1985-07-05", NULL, NULL),
    ("Dr. Abhira Potadar", 7685033458, "ap@gmail.com", "A+", "Dermatologist", "1974-08-06", NULL, NULL),
    ("Dr. Kartik Goenka", 9878645673, "kg@gmail.com", "O+", "Radiologist", "1965-07-03", NULL, NULL),
    ("Dr. Abhimanu Birla", 8796546843, "ab@gmail.com", NULL, "Orthopedist", "1969-11-24", NULL, NULL),
    ("Dr. Ramya Dixit", 7856490786, "rd@gmail.com", NULL, "Surgion", "1965-03-06", NULL, NULL),
    ("Dr. Aradhya Dev", 8945725683, "ad@gmail.com", NULL, "Physicians", "1960-01-01", NULL, NULL),
    ("Dr. Devansh Gupta", 9076890997, "dg@gmail.com", NULL, "Allergist", "1984-04-06", NULL, NULL);

select * from doctor;

CREATE TABLE Appointment (
    App_id INT PRIMARY KEY AUTO_INCREMENT,
    Doc_id INT,  -- Add this line to include the Doc_id column
    Pat_id INT,  -- Add this line to include the Pat_id column
    App_Date_of_Appointment VARCHAR(50),
    App_Time_of_Appointment VARCHAR(25),
    INDEX idx_App_id (App_id),
    
    INDEX idx_Doc_id (Doc_id),
    INDEX idx_Pat_id (Pat_id),
    FOREIGN KEY (Doc_id) REFERENCES Doctor(Doc_id),
    FOREIGN KEY (Pat_id) REFERENCES Patient(Pat_id)
);
INSERT INTO Appointment (Doc_id, Pat_id, App_Date_of_Appointment, App_Time_of_Appointment)
VALUES (1, 1, '2023-01-15', '10:00 AM');

#select * from doctor;

CREATE USER 'Kedar'@'localhost' IDENTIFIED BY '1234567';

SELECT user, host FROM mysql.user WHERE user = 'Kedar';#This will show you the host(s) associated with the 'Kedar' user.

#Syntax: SELECT user, host FROM mysql.user;
#Remember to run these queries with a user account that has the necessary privileges to access the mysql database and user table, such as the MySQL root user.

GRANT ALL PRIVILEGES ON *
.* TO 'Kedar'@'localhost';
commit;