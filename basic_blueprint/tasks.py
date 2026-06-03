from flask import Blueprint, jsonify
from database import db, Task

# Create the blueprint
tasks_bp = Blueprint('tasks', __name__)

# Route 1: View all tasks from the database
@tasks_bp.route('/')
def get_tasks():
    all_tasks = Task.query.all()

    task_list = [
        {"id": task.id, "title": task.title}
        for task in all_tasks
    ]

    return jsonify(task_list)

# Route 2: Add a new task to the database
@tasks_bp.route('/add/<string:name>')
def add_task(name):
    new_task = Task(title=name)

    db.session.add(new_task)
    db.session.commit()

    return jsonify({
        "message": f"Task '{name}' saved successfully!"
    })