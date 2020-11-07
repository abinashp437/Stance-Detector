from flask import Flask, request, jsonify, render_template
import json
from flask_cors import CORS
import pickle
import pandas as pd
import numpy as np
import nltk
nltk.download('stopwords') #for stopword removal
nltk.download('wordnet')
from nltk.corpus import stopwords
from gensim.models import Word2Vec
import tensorflow as tf
from tensorflow import keras

app = Flask(__name__)
CORS(app)

stop_words = stopwords.words('english')
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()
pad_art = 180
pad_head = 11

def n_removal(text):
    return text.replace('\n','')

def stopword_removal(text):
    return ' '.join([word for word in text.split() if word not in stop_words])

def lemmatization(text):
    return ' '.join([lemmatizer.lemmatize(word) for word in w_tokenizer.tokenize(text)])

def case_lower(text):
    return text.lower()

def trim_line(text, pad):
    return ' '.join(w_tokenizer.tokenize(text)[:pad])

def preprocessed(text):
    text = n_removal(text)
    text = stopword_removal(text)
    text = lemmatization(text)
    text = case_lower(text)
    return text

def vectorise(text):
    vec = Word2Vec.load('vector.bin')
    vectors = [vec[word] for word in w_tokenizer.tokenize(text)]
    return vectors


@app.route('/')
def webprint():
    return render_template('predict.html')

@app.route('/detect', methods=['POST'])
def obtain():
    article = request.form['article']
    headline = request.form['headline']
    print(article)
    print(headline)
    stance = jsonify(predictor(article, headline)) #answer = preprocessed attribute
    stance.headers.add('Access-Control-Allow-Origin', '*')
    return stance

def predictor(art, head):
    art = preprocessed(art)
    head = preprocessed(head)
    art = trim_line(art, pad_art)
    head = trim_line(head, pad_head)
    art_vec = vectorise(art)
    head_vec = vectorise(head)
    test = [head_vec, art_vec]
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