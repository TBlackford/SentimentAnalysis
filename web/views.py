from flask import render_template, request, redirect
from flask_restplus import Resource, Namespace
from . import app, api
import random, logging

def get_sentiment(word=""):
    return random.randint(0,100)

###################################################################################
# Simple pages

@app.route('/')
def index_page():
    return render_template('index.html')

###################################################################################
# API Namespace

ns = Namespace('api', description='API Operations')

@ns.route('/sentiment', methods=['POST'])
class ShowUploadedFiles(Resource):
    def post(self):
        #logging.warning(request.form["word"])

        word = request.form["word"]

        # Get the sentiment value
        value = get_sentiment(word)

        return {"sentiment": value}

api.add_namespace(ns)
