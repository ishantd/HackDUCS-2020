from flask import Flask, render_template, Response, jsonify, request, send_file
# from camera import VideoCamera
from flask_sqlalchemy import  SQLAlchemy
import cv2
import numpy as np
# from keras.models import model_from_json
# from keras.preprocessing import image
from io import BytesIO





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ishant/ishant_linux/hackDUCS/database/filesstorage.db'
db = SQLAlchemy(app)

images_url = []

for i in range(97,123):
    images_url.append('images/'+ chr(i) +'.jpg')

def split(word): 
    return [char for char in word]  




class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fileName = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)



