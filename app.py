print("App is starting...")
from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        dbname="student_portal_db",
        user="postgres",
        password="1234",  
        host="localhost",
        port="5432"
    )

    
from flask import redirect

@app.route('/')
def home():
    return redirect('/students')

@app.route('/students')
def students():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM students")
    students = cur.fetchall()
    
    cur.close()
    conn.close()

    return render_template('students.html', students=students)


@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            return "All fields required!"

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO students (name, email) VALUES (%s, %s)",
            (name, email)
        )

        conn.commit()
        cur.close()
        conn.close()
        return redirect('/students')

    return render_template('add_student.html')

@app.route('/students/<int:id>/edit', methods=['GET', 'POST'])
def edit_student(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        cur.execute(
            "UPDATE students SET name=%s, email=%s WHERE id=%s",
            (name, email, id)
        )

        conn.commit()
        cur.close()
        conn.close()

        return redirect('/students')

    cur.execute("SELECT * FROM students WHERE id=%s", (id,))
    student = cur.fetchone()

    cur.close()
    conn.close()

    return render_template('edit_student.html', student=student)


@app.route('/students/<int:id>/delete', methods=['POST'])
def delete_student(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=%s", (id,))
    
    conn.commit()
    cur.close()
    conn.close()

    return redirect('/students')



def get_grade_letter(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'
    
    
@app.route('/grades')
def grades():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT grades.id, students.name, units.name, grades.score
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN units ON grades.unit_id = units.id
    """)

    grades = cur.fetchall()
    cur.close()
    conn.close()

    return render_template('grades.html', grades=grades)

@app.route('/grades/add', methods=['GET', 'POST'])
def add_grade():
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        student_id = request.form['student_id']
        unit_id = request.form['unit_id']
        score = int(request.form['score'])

        letter = get_grade_letter(score)

        cur.execute("""
            INSERT INTO grades (student_id, unit_id, score)
            VALUES (%s, %s, %s)
        """, (student_id, unit_id, score))

        conn.commit()
        cur.close()
        conn.close()
        return redirect('/grades')

    cur.execute("SELECT * FROM students")
    students = cur.fetchall()

    cur.execute("SELECT * FROM units")
    units = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('add_grade.html', students=students, units=units)

@app.route('/grades/<int:id>/edit', methods=['GET', 'POST'])
def edit_grade(id):
    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        score = int(request.form['score'])

        cur.execute("""
            UPDATE grades SET score=%s WHERE id=%s
        """, (score, id))

        conn.commit()
        cur.close()
        conn.close()
        return redirect('/grades')

    cur.execute("SELECT * FROM grades WHERE id=%s", (id,))
    grade = cur.fetchone()

    cur.close()
    conn.close()

    return render_template('edit_grade.html', grade=grade)

@app.route('/grades/<int:id>/delete', methods=['POST'])
def delete_grade(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM grades WHERE id=%s", (id,))

    conn.commit()
    cur.close()
    conn.close()

    return redirect('/grades')

@app.route('/dashboard')
def dashboard():
    conn = get_db_connection()
    cur = conn.cursor()


    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]


    cur.execute("SELECT AVG(score) FROM grades")
    avg_score = cur.fetchone()[0]

    cur.execute("""
        SELECT students.name, AVG(grades.score) as avg_score
        FROM grades
        JOIN students ON grades.student_id = students.id
        GROUP BY students.name
        ORDER BY avg_score DESC
        LIMIT 1
    """)
    top_student = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        'dashboard.html',
        total_students=total_students,
        avg_score=round(avg_score, 2) if avg_score else 0,
        top_student=top_student
    )

@app.route('/students/<int:id>/grades')
def student_grades(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT units.name, grades.score
        FROM grades
        JOIN units ON grades.unit_id = units.id
        WHERE grades.student_id = %s
    """, (id,))

    grades = cur.fetchall()

    cur.close()
    conn.close()

    return render_template('student_grades.html', grades=grades)


from flask import jsonify

@app.route('/chart-data')
def chart_data():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT students.name, AVG(grades.score)
        FROM grades
        JOIN students ON grades.student_id = students.id
        GROUP BY students.name
    """)

    data = cur.fetchall()

    cur.close()
    conn.close()

    labels = [row[0] for row in data]
    values = [float(row[1]) for row in data]

    return jsonify({
        'labels': labels,
        'values': values
    })
    
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

@app.route('/download_pdf')
def download_pdf():
    
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, "Student Grades Report")

    # Connect to database
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT students.name, units.name, grades.score
        FROM grades
        JOIN students ON grades.student_id = students.id
        JOIN units ON grades.unit_id = units.id
        ORDER BY students.name
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()

    
    y = height - 100
    c.setFont("Helvetica", 12)
    c.drawString(50, y, "Student")
    c.drawString(250, y, "Unit")
    c.drawString(400, y, "Score")
    y -= 20

    for row in data:
        c.drawString(50, y, str(row[0]))
        c.drawString(250, y, str(row[1]))
        c.drawString(400, y, str(row[2]))
        y -= 20
        if y < 50:
            c.showPage()
            y = height - 50

    c.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="grades_report.pdf", mimetype='application/pdf')

def calculate_gpa(grades):
    """
    Calculate GPA from a list of grades.

    Parameters:
        grades (list of float): List of numeric grades.

    Returns:
        float: GPA rounded to two decimal places.
    """
    if not grades:
        return 0.0
    return round(sum(grades) / len(grades), 2)




if __name__ == "__main__":
    app.run(debug=True)