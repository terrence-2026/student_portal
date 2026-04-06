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
 
 <img width="1216" height="881" alt="Screenshot 2026-04-06 183902" src="https://github.com/user-attachments/assets/973beeb5-bca9-4e32-b6c7-413367ee7063" />
 <img width="1389" height="511" alt="Screenshot 2026-04-06 183914" src="https://github.com/user-attachments/assets/bf4c695f-048c-48bc-b52c-097afc64db26" />
 <img width="1261" height="282" alt="Screenshot 2026-04-06 183929" src="https://github.com/user-attachments/assets/22da74f9-3387-4134-87cb-1e06ea984bef" />
 <img width="1515" height="652" alt="Screenshot 2026-04-06 184128" src="https://github.com/user-attachments/assets/bbb5bcd2-8080-42f7-b626-bafdcca4fc8c" />
 <img width="1308" height="466" alt="Screenshot 2026-04-06 184142" src="https://github.com/user-attachments/assets/3726210e-760a-4eaf-9755-6f7de12c305b" />
 <img width="1919" height="939" alt="Screenshot 2026-04-06 184236" src="https://github.com/user-attachments/assets/6837b045-2862-4aff-84fb-1b584dc4bb00" />
 <img width="1176" height="654" alt="Screenshot 2026-04-06 184247" src="https://github.com/user-attachments/assets/03e27564-3b1a-4a25-b693-e75868546947" />
 <img width="1901" height="718" alt="Screenshot 2026-04-06 184324" src="https://github.com/user-attachments/assets/f4fe00a3-36ed-4cb8-b4dd-5186a2ca0649" />
















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
