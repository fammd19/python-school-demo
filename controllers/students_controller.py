from flask_restful import Resource
from models import db, Student, Course, Enrolment
from flask import make_response, request


class Students(Resource):
    
    def get(self):
        students = [ student.to_dict() for student in Student.query.all() ]

        return make_response(students, 200)

    def post(self):
        new_student = Student (
            name = request.json['name'],
            degree = request.json['degree']
        )

        db.session.add(new_student)
        db.session.commit()

        if new_student.id:
            return make_response(new_student.to_dict(), 201)

        else:
            return make_response({"error":"Student not created"}, 403)

class StudentById(Resource):

    # @classmethod
    # def find_student(cls, id):
    #     return Student.query.filter(Student.id == id).first()

    def get(self, id):
        student = Student.query.filter(Student.id == id).first()

        if student:
            return make_response(student.to_dict(), 200)
        
        else:
            return make_response({"error":"Student not found"}, 403)

    def patch(self, id):
        student = Student.query.filter(Student.id == id).first()

        if student:

            for attr in request.json:
                setattr(student, attr, request.json[attr])

            db.session.commit()

            return make_response(student.to_dict(), 200)
        
        else:
            return make_response({"error":"Student not found"}, 403)

    def delete(self, id):
        student = Student.query.filter(Student.id == id).first()

        if student:
            db.session.delete(student)

            db.session.commit()

            return make_response({"message":"Student deleted"}, 204)

        else:
            return make_response({"errro":"Student not found"}, 403)


class StudentEnrol(Resource):

    def post(self, id):

        student = Student.query.filter(Student.id == id).first()

        if student:

            course = Course.query.filter(Course.id == request.json['course_id']).first()

            if course:

                #add a checker to see if student is already enroled in the course

                new_enrolment = Enrolment (
                    student_id = student.id,
                    course_id = course.id
                )

                db.session.add(new_enrolment)
                db.session.commit()

                return make_response({"message":"Successfully enrolled"}, 201)
            
            else:
                return make_response({"error":"No course found"}, 403)

        else:
            return make_response({"error":"Student not found"}, 403)