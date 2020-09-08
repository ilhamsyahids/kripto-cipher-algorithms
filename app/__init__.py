from flask import Flask, render_template
from flask_cors import CORS, cross_origin


app = Flask(__name__, template_folder="static")
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')