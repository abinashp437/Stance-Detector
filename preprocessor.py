import nltk
# nltk.download('stopwords') #for stopword removal
# nltk.download('wordnet') #for lemmatization
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from tensorflow import keras


stop_words = stopwords.words('english')
w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
lemmatizer = nltk.stem.WordNetLemmatizer()


def preprocess(text):
    n_rem = text.replace('\n','')
    st_wo = ' '.join([word for word in n_rem.split() if word not in stop_words])
    lem = ' '.join([lemmatizer.lemmatize(word) for word in w_tokenizer.tokenize(st_wo)])
    low = lem.lower()
    print('\n\n\n low',low,'\n\n\n')
    return low

def trim_line(text, pad):
    trim = ' '.join(w_tokenizer.tokenize(text)[:pad])
    return trim

def vectorise(vec, pad):
    w_tokenizer = nltk.tokenize.WhitespaceTokenizer()
    vect = Word2Vec.load('vector.bin')
    vectors = [vect[word] for word in w_tokenizer.tokenize(vec)]
    pad_vec = keras.preprocessing.sequence.pad_sequences(vec, padding = 'post', maxlen = pad, dtype = float)
    pad_vec_list = pad_vec.tolist()
    print(len(pad_vec_list))
    return pad_vec_list