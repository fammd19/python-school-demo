from flask_restful import Resource
from models import db, Course
from flask import make_response, request

class Courses(Resource):
    #becomes a parent class - abstarct class - courses will inherit from here

    def get(self):
        #instance vairable so pass self
        #automnatically points to /courses through the api call 
        courses = [ course.to_dict() for course in Course.query.all() ]

        return make_response(courses, 200)

    def post(self):
        new_course = Course(title=request.json['title'])
        db.session.add(new_course)
        db.session.commit()

        if new_course.id:
            return make_response(new_course.to_dict(), 201)

        else:
            ({"error":"create unsuccessful"}, 403)


class CourseById(Resource):

    #/course/<int:id>
    def get(self, id):
        course = Course.query.filter(Course.id == id).first()

        if course:
            return make_response(course.to_dict(), 200)

        else:
            return make_response({"error":"No course found"}, 404)






