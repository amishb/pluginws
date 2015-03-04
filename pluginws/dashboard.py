#!/usr/local/bin/virtualenv
from flask import Flask, jsonify


# Sets variables that we need

ver = 0.2
modules = [
    {
        'route': '/',
        'name': 'Version',
        'description': 'Prints the version of the software'
    },
    {
        'route': '/modules',
        'name': 'Loaded modules',
        'description': 'Prints all the modules loaded'
    }
]

app = Flask(__name__)

@app.route('/')
def version():
    return jsonify(version=ver)

@app.route('/modules')
def list_modules():
    return jsonify(results=modules)

@app.route('/stats')
def stats():
    return jsonify(id=2, name='john')


