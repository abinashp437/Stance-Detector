from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import preprocessor as pr


app = Flask(__name__)
CORS(app)


@app.route('/')
def webprint():
    return render_template('predict.html')

@app.route('/detect', methods=['POST'])
def obtain():
    article = request.form['article']
    headline = request.form['headline']
    pad_art = 180
    pad_head = 11
    pre_art = pr.preprocess(article)
    pre_head = pr.preprocess(headline)
    trim_art = pr.trim_line(pre_art, pad_art)
    trim_head = pr.trim_line(pre_head, pad_head)
    art_vec = pr.vectorise(trim_art, pad_art)
    head_vec = pr.vectorise(trim_head, pad_head)
    stance = jsonify(predictor(art_vec, head_vec)) #answer = preprocessed attribute
    stance.headers.add('Access-Control-Allow-Origin', '*')
    return stance

def predictor(art_vec, head_vec):
    head_test = tf.convert_to_tensor(head_vec)
    art_test = tf.convert_to_tensor(art_vec)
    test = [head_test, art_test]
    classifier = pickle.load(open('model.h5','rb'))
    stance = classifier.predict(test)
    print(stance)
    if stance[0] == 0:
        result = 'unrelated'
    elif stance[0] == 1:
        result = 'agree'
    elif stance[0] == 2:
        result = 'disagree'
    elif stance[0] == 3:
        result = 'discuss'
    ret = {'type' : "JSON/TXT"}
    ret['stance'] = str(result)
    print(ret)
    return ret



app.run(port=8787, debug=True)