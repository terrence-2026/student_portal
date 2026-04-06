# Student Portal Web App

A simple Flask web application to manage students, grades, and generate transcripts.

## Technologies Used

- Python 3.11
- Flask 2.3
- PostgreSQL 15
- psycopg2-binary
- ReportLab 4.0
- HTML/CSS/Bootstrap 5


 ##screenshots
<img width="1899" height="923" alt="screen shot 1" src="https://github.com/user-attachments/assets/677626a1-9fb9-4f34-9224-0960a9d42b3e" />
<img width="1857" height="937" alt="image" src="https://github.com/user-attachments/assets/007f5568-e4a0-4baf-a14b-3cc1bf2d3da0" />
<img width="1915" height="830" alt="image" src="https://github.com/user-attachments/assets/8d4af5dc-7622-4fdd-966e-bb03cd082f47" />
<img width="1367" height="534" alt="Screenshot 2" src="https://github.com/user-attachments/assets/bc763c17-95c5-413b-851e-9cde2b468658" />
<img width="1910" height="894" alt="image" src="https://github.com/user-attachments/assets/38ae54ba-2fc3-42d7-b06c-555896b00eb6" />
<img width="1903" height="816" alt="image" src="https://github.com/user-attachments/assets/a2c2b0d7-3b6a-4bde-9a7b-aa946392200b" />
<img width="1897" height="1056" alt="Screenshot 3" src="https://github.com/user-attachments/assets/1b8d23d9-e273-44dd-8a93-0290f5a05f89" />
<img width="1110" height="532" alt="image" src="https://github.com/user-attachments/assets/52f6a796-efe5-40ac-9901-7caf6a097904" />
<img width="1145" height="773" alt="Screenshot 2026-04-06 012353" src="https://github.com/user-attachments/assets/f353e8cf-3304-4c9b-91f7-a5b1999203be" />







##setup instruction
1. Clone the repository:
   ```bash
   git clone https://github.com/terrence-2026/student_portal.git
2. Create and activate a virtual environment
python -m venv venv

Windows:
venv\Scripts\activate


3. Install dependencies
pip install -r requirements.txt
4. Set up environment variables

Create a .env file in the root directory and add:

DB_HOST=localhost
DB_NAME=student_portal
DB_USER=postgres
DB_PASS=Mwalim

5. Create PostgreSQL database

Open PostgreSQL and run:

CREATE DATABASE student_portal;
6. Run database schema
psql -U postgres -d student_portal -f schema.sql
7. Run the application
flask run

Then open your browser and go to:

http://127.0.0.1:5000/students
http://127.0.0.1:5000/grades
http://127.0.0.1:5000/students/1/grades
http://127.0.0.1:5000/dashboard

# Features
1. Student Management
Add new students
View all students
Update student details
Delete students
2. Grade Management
Record student grades
View grades per student
Calculate performance
3. Analytics Dashboard
Visualize student performance using Chart.js
Display grade distributions
4. PDF Transcript Generation
Generate downloadable student transcripts using ReportLab
5. Input Validation & Error Handling
Server-side validation for all forms
Safe database operations using try/except

# Project Structure
student_portal/
│── app.py
│── schema.sql
│── requirements.txt
│── .env.example
│── templates/
│── static/
│── README.md
│── .gitignore

 #Author
Name: Terrence Omondi
Student Number: 2600298

 #License

This project is for academic purposes only.
