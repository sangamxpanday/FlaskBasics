from flask_sqlalchemy import SQLAlchemy

# Create the database object
db = SQLAlchemy()

# Define how a Task looks in the database
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)