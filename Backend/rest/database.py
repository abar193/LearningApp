from flask import Flask, request, send_from_directory, jsonify
import _sqlite3
import os

__courses = {
    '0': {'name': 'Learning "Learning App"', 'description': 'Guide to our app',
          'lectures': [{'id': '001', 'name': 'Demo'}, {'id': '002', 'name': 'Other demo'}]},
    '1': {'name': 'Programming course', 'description': 'Because we all really need it :(',
          'lectures': [{'id': '001', 'name': 'Contentful API'}]}
}

__notes = {
    '0-001': [
        {'question': 'What is a "Learning app"?', 'answer': 'Learning app is our hackaton project, which aims on helping students with self-study'},
        {'question': 'How does it works?', 'answer': 'It allows user to organize his learning notes, and then go through them in a self test'}
    ],
    '0-002': [
        {'question': 'To be or not to be?', 'answer': 'That is the question'}
    ],
    '1-001': []
}

def get_courses():
    return __courses


def create_course(data):
    i = str(__courses.__len__())
    data['lectures'] = []
    __courses[i] = data

def get_notes(id):
    return __notes[id]


def create_note(noteid, note):
    __notes[noteid].append(note)
