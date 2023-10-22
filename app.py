from flask import Flask, render_template, request, url_for, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://breadlover:admin@cluster0.lieum6u.mongodb.net/SE2_666?retryWrites=true&w=majority'
mongo = PyMongo(app)

todos = mongo.db.todos

@app.route('/')
def index():
    saved_todos = todos.find()
    return render_template('add_course.html', todos=saved_todos)

