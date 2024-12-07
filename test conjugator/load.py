from flask import Flask, jsonify, request, render_template,url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/qutrub', methods=['GET'])
def get_qutrub_response():
    verb = request.args.get('verb')
    haraka = request.args.get('haraka', '')
    trans = request.args.get('trans', '')

    qutrub_url = f'http://qutrub.arabeyes.org/api?verb={verb}'
    if haraka:
        qutrub_url += f'&haraka={haraka}'
    if trans:
        qutrub_url += f'&trans={trans}'

    response = requests.get(qutrub_url)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)