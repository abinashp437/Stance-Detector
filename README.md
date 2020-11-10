# Stance-Detector

## Getting Started
```
Git clone or download this Project as zip
Execute the following commands in the base directory
```
### Prerequisites for notebooks
```
The notebooks are in google colab so can be directly executed in colab or jupyter notebok can be used for the same
```

### Prerequisites for Detection

* install python3
* install pip3
* install venv using pip
```
pip3 install venv
```
* Create a Virtual environment, install depedencies in the base directory of the project:-
```
python3 -m venv venv
source venv/bin/activate(for ubuntu)
venv/Scripts/activate(for windows)
pip install tensorflow(version 2.0x)
pip install flask
pip install flask_cors
pip install nltk
pip install pandas
python -m nltk.downloader wordnet
python -m nltk.downloader stopwords
deactivate
```
The above steps are needed to be performed only the first time.


## Running the Program
```
Download  vector.bin by executing the fnc_1.ipynb
Download model_lstm.h5 by executing the lstm_fnc.ipynb
save both the folders in the base directory
```
* Server:
```
source venv/bin/activate
python prediction.py
```

* When it shows The app in running in port 8787
Open your browser and goto
```
localhost:8787
```
* Later, the virtual environment can be deactivated when the work with project is over
```
deactivate
```


## Built With

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The web framework used
* [Javascript](https://devdocs.io/javascript/) - used for scripting
* [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - It is the templating library used
* [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS) - It is used for styling purpose


## Authors

* **Abinash Panda** - AI Developer(https://github.com/abinashp437)
