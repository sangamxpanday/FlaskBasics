from flask import Flask, jsonify, request

app = Flask(__name__)

# Fake Database
students = [
    {
        "id": 1,
        "name": "Sangam"
    },
    {
        "id": 2,
        "name": "Ram"
    }
]

# GET ALL STUDENTS
@app.route('/students', methods=['GET'])
def get_students():

    return jsonify(students)


# GET ONE STUDENT
@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):

    for student in students:

        if student['id'] == id:
            return jsonify(student)

    return jsonify({
        "message": "Student not found"
    }), 404


# CREATE STUDENT
@app.route('/students', methods=['POST'])
def create_student():

    data = request.json

    new_student = {
        "id": len(students) + 1,
        "name": data['name']
    }

    students.append(new_student)

    return jsonify({
        "message": "Student created",
        "student": new_student
    }), 201


# UPDATE STUDENT
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):

    data = request.json

    for student in students:

        if student['id'] == id:

            student['name'] = data['name']

            return jsonify({
                "message": "Student updated",
                "student": student
            })

    return jsonify({
        "message": "Student not found"
    }), 404


# DELETE STUDENT
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):

    for student in students:

        if student['id'] == id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted"
            })

    return jsonify({
        "message": "Student not found"
    }), 404


if __name__ == '__main__':
    app.run(debug=True)