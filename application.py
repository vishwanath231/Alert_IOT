from flask import Flask, request, jsonify
from funcs import current_time, insert_one, read_documents, update_document
from flask_cors import CORS


application = Flask(__name__)


CORS(application)

@application.route('/')
def home():

    return "Hello World"


@application.route('/insert', methods=['POST'])
def insert():
    post = request.json
    insert_one(post)
    return jsonify({"message": "Document inserted successfully"}), 201

@application.route('/read', methods=['GET'])
def read():
    query = request.args.to_dict()
    documents = read_documents(query)
    my_data  ={}
    my_data['data'] = documents
    return jsonify(my_data), 200


@application.route('/update/<document_id>', methods=['PUT'])
def update(document_id):
    update_values = request.json
    modified_count = update_document(document_id, update_values)
    return jsonify({"modified_count": modified_count}), 200

if __name__ == "__main__":
    application.run(debug=True)
