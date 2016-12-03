from flask import Flask, request, send_from_directory, jsonify
import rest.database as database
import os

app = Flask(__name__)

if os.path.isdir('./src'):
    ROOT_DIR = './src/'
else:
    ROOT_DIR = '../../src/'

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory(ROOT_DIR + 'js', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory(ROOT_DIR + 'css', path)

@app.route('/index')
def send_main():
    return send_from_directory(ROOT_DIR, 'index.html')

@app.route('/save')
def send_save():
    return send_from_directory(ROOT_DIR, 'save.html')

@app.route('/selftest')
def send_test():
    return send_from_directory(ROOT_DIR, 'selftest.html')


@app.route('/api/courses')
def get_courses():
    return jsonify(database.get_courses())

@app.route('/api/courses', methods=['POST'])
def post_course():
    data = request.json
    database.create_course(data)
    return jsonify(database.get_courses())

@app.route('/api/lectures/<courseid>')
def get_lectures(courseid):
    return jsonify(database.get_lectures(courseid))

@app.route('/api/lectures/<courseid>', methods=['POST'])
def post_lecture(courseid):
    data = request.json
    database.create_lecture(courseid, data)
    return jsonify(database.get_lectures(courseid))

@app.route('/api/notes/<lectureid>')
def get_notes(lectureid):
    return jsonify(database.get_notes(lectureid))

@app.route('/api/notes/<lectureid>', methods=['POST'])
def post_note(lectureid):
    data = request.json
    database.create_note(lectureid, data)
    return jsonify(database.get_notes())

@app.route('/api/debug')
def debug():
    print(database.__courses)
    print(database.__lectures)
    print(database.__notes)
    return jsonify(database.__notes)

if __name__ == "__main__":
    print(os.listdir(ROOT_DIR))
    app.run()
