from flask import Flask, jsonify, request, make_response
from flask_restful import Resource, Api, reqparse
from flask_pymongo import PyMongo
import os, sys
import requests, json
from functools import wraps
# from config import Config
from config import *
import pandas as pd


app = Flask(__name__)

# app.config.from_object(Config)

# # Database
# mongo = PyMongo(app)

# mongo1 = PyMongo(app, os.environ.get('MONGO_URI'))

# mongo2 = PyMongo(app, os.environ.get('MONGO_URI_1'))

# mongo3 = PyMongo(app, os.environ.get('MONGO_URI_2'))