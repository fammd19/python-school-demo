from flask import Blueprint, request, jsonify, make_response
from models import db, Student, Enrolment, Course

course_bp = Blueprint('course', __name__, url_prefix="/courses")


@course_bp.route('/')
def index():
    courses_from_db = Course.query.all()

    courses = []

    for course in courses_from_db:
        courses.append(course.to_dict())

    return make_response(jsonify(courses), 200)


@course_bp.route('/', methods=['POST'])
def create():
    new_course= Course(title=request.json['title'])
    db.session.add(new_course)
    db.session.commit()

    if new_course.id:
        return make_response(jsonify(new_course.to_dict()), 201)

    return make_response(jsonify({"error":"Error in creating"}), 403)

@course_bp.route('/<int:course_id>')
def show_by_id(course_id):
    course = Course.query.filter(Course.id == course_id).first()

    if course:
        return make_response(jsonify(course.to_dict()), 201)

    return make_response(jsonify({"error":"No course found"}), 403)

@course_bp.route('/<int:course_id>', methods=["PATCH", "PUT"])
def update(course_id):
    course = Course.query.filter(Course.id == course_id).first()

    if course:
        for attr in request.json:
            setattr(course, attr, request.json[attr])
        
        db.session.commit()

        return make_response(jsonify(course.to_dict()), 200)

    return make_response(jsonify({"error":"Error"}), 403)

@course_bp.route('/<int:course_id>', methods=["DELETE"])
def destroy(course_id):
    course = Course.query.filter(Course.id == course_id).first()

    if course:
        db.session.delete(course)
        db.session.commit()

        return make_response(jsonify({"message":"Course deleted"}), 200)

    return make_response(jsonify({"error":"Error"}), 403)

# Routes
# GET    / - Return all classes
# POST   / - Create a new class
# GET    /:class_id - Return class with class_id
# PATCH  /:class_id - Update the class with class_id
# DELETE /:class_id - Delete class with class_id
# GET    /:class_id/students - Return all students from the class with class_id

@course_bp.route('/<int:course_id>/students')
def get_course_students(course_id):
    course = Course.query.filter(Course.id == course_id).first()

    
    if course:
        students = []

        for student in course.students:
            students.append(student.to_dict())

        return make_response(jsonify(students), 20)

    return make_response(jsonify({"error":"Course not found"}), 403)