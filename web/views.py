from flask import render_template
from flask_restplus import Resource, Namespace
from . import app, api

###################################################################################
# Simple pages

@app.route('/')
def index_page():
    return render_template('index.html')


###################################################################################
# API Namespace

ns = Namespace('api', description='API Operations')

@ns.route('/upload_files')
class ShowUploadedFiles(Resource):
    def post(self):

        # asdf

        return {"universities": "etc"}

api.add_namespace(ns)