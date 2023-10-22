from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
import os

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb+srv://breadlover:admin@cluster0.lieum6u.mongodb.net/SE2_666?retryWrites=true&w=majority"
mongo = PyMongo(app)
courses = mongo.db.courses
professors = mongo.db.courses

@app.route('/')
def show_home():
   return render_template('main_screen.html')

@app.route('/add')
def show_add():
    return render_template('add_course.html', message = "")

@app.route('/add', methods=['POST'])
def add_course():
    course_id = request.form.get('courseId')
    course_name = request.form.get('courseName')
    professor_name = request.form.get('professorName')
    course_location = request.form.get('courseLocation')
    
    doc = {
        "course_id": course_id,
        "course_name": course_name,
        "professor_name": professor_name,
        "course_location": course_location
    }

    courses.insert_one(doc)

    return render_template('add_course.html', message="Added Successfully")


@app.route('/delete')
def show_delete():
    return render_template('delete_course.html', message = "")

@app.route('/delete', methods=['POST'])
def delete_course():
    course_id = request.form['courseId']
    doc = courses.find_one({"course_id": course_id})
    if doc is not None:
        courses.delete_one({"course_id": course_id})
        return render_template('delete_course.html', message = "Deleted Successfully")
    else:
        return render_template('delete_course.html', message = "Error: Course Not Existed")

@app.route('/verify_id')
def show_verify():
    return render_template('edit_course_verify.html', message = "")

@app.route('/verify_id', methods=['POST'])
def check_id():
    course_id = request.form['courseId']
    if courses.find_one({"course_id": course_id}) is None:
        return render_template('edit_course_verify.html', message = "Error: Course Not Existed")
    else:
        return redirect(url_for('show_edit'), id = course_id)

@app.route('/edit/<string:id>')
def show_edit(id):
    return render_template('edit_course_edit.html', course_id = id, message = "")

@app.route('/edit/<string:id>', methods=['POST'])
def edit_course(id):
    course_name = request.form['courseName']
    professor_name = request.form['professorName']
    course_location = request.form['courseLocation']
    update = {}
    if course_name:
        update["course_name"] = course_name
    if professor_name:
        update["professor_name"] = professor_name
    if course_location:
        update["course_location"] = course_location
    courses.update_one({'course_id': id}, {"$set": update})
    return render_template('edit_course_edit.html', course_id = id, message = "Edit Successfully")

@app.route('/retrive_professors')
def show_profs():
    docs = professors.find({}).sort('name', 1)
    return render_template('browse_professors.html', docs = docs)

@app.route('/retrive_courses')
def show_courses():
    docs = courses.find({}).sort('course_name', 1)
    return render_template('browse_professors.html', docs = docs)

@app.route('/search')
def show_search():
    render_template("search_course.html", docs = None, message ="")

@app.route('/search', methods=['POST'])
def search_course():
    course_id = request.form['courseId']
    docs = courses.find({"course_id": course_id})
    if docs is not None:
        return render_template("search_course.html", docs = docs, message ="")
    else:
        render_template("search_course.html", docs = None, message ="Error: Course Not Existed")