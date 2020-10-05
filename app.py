import os
from flask import Flask, escape, request
from bert import Bert
from flask import jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/json', methods=['POST'])
def my_json():
    json_dict = request.get_json()
    question = json_dict['question']
    bert = Bert(question)
    predict_class = bert.predict()
    # data = {'answer': predict_class}
    return predict_class


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='140.115.197.241', port=port)
