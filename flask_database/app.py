from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Model (Table)
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


# Create tables
with app.app_context():
    db.create_all()


# Form Page
@app.route('/')
def home():
    return render_template('form.html')


# Save Data
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    student = Student(
        name=name,
        email=email
    )

    db.session.add(student)
    db.session.commit()

    return redirect('/view')


# View All Records
@app.route('/view')
def view():
    students = Student.query.all()
    return render_template(
        'view.html',
        students=students
    )


if __name__ == '__main__':
    app.run(debug=True)