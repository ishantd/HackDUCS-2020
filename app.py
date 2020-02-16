from flask import Flask, render_template, Response, jsonify, request, send_file
# from camera import VideoCamera
# from flask_sqlalchemy import  SQLAlchemy
# import cv2
# import numpy as np
# from keras.models import model_from_json
# from keras.preprocessing import image
# from io import BytesIO

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/ishant/ishant_linux/boongg_project/web_api/database/filesstorage.db'
# db = SQLAlchemy(app)


# ===================FOR DEVELOPMENT ONLY=================
app.debug = True
# =========================================

# class FileContents(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     fileName = db.Column(db.String(300))
#     data = db.Column(db.LargeBinary)

@app.route('/ocr2sign')
def ocr2sign():
    return render_template('ocr2sign.html')

@app.route('/txt2sign')
def txt2sign():
    return render_template('txt2sign.html')



@app.route('/')
def index():
    return render_template('welcome.html')





# --bottom--
if __name__ == '__main__':
    app.run(threaded=False)
