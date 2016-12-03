from flask import Flask, request, send_from_directory, jsonify
import _sqlite3
import os

__courses = {
    '0': {'name': 'Learning "Learning App"', 'description': 'Guide to our app'},
    '1': {'name': 'Programming course', 'description': 'Because we all really need it :('}
}

__lectures = {
    '0': [{'id': '001', 'name': 'Demo'}, {'id': '002', 'name': 'Other demo'}],
    '1': [{'id': '001', 'name': 'Introducing to contentful'}]
}

__notes = {
    '0-001': [
        {'question': 'What is a "Learning app"?', 'answer': 'Learning app is our hackaton project, which aims on helping students with self-study'},
        {'question': 'How does it works?', 'answer': 'It allows user to organize his learning notes, and then go through them in a self test'}
    ],
    '0-002': [],
    '1-001': []
}

def get_courses():
    return __courses


def create_course(data):
    i = str(__courses.__len__())
    __courses[i] = data
    __lectures[i] = []

def get_lectures(course_id):
    return __lectures[course_id]


def create_lecture(course, data):
    id = course + "-" + "%03d" % __lectures[course].__len__()
    __lectures[course].append(data)
    __notes[id] = []

def get_notes(lecture_id):
    return __notes[lecture_id]


def create_note(noteid, note):
    __notes[noteid].append(note)
