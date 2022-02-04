
# create a web API that provides programmatic access to json data.
# please run index_json_file.py first to load data
# Qin Zhang 02/03/2022

from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

import json

es = Elasticsearch()

app = Flask(__name__)
app.config['DEBUG'] = True

index_name = 'myindex'
type_name = 'mydataset'

# Get data by the '@id' field in the data
# i.e. localhost:5000/query_id?id=https://doi.org/10.11588/data/0HJAJS

@app.route('/query_id', methods=['GET'])
def api_get_by_id():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return 'Error: No id field provided. Please specify an id.'

    result = es.get(index=index_name, doc_type=type_name, id=id)
    return jsonify(result)

# query by a field in the JSON data
# i.e. localhost:5000/query?keywords=Earth and Environmental Sciences
# i.e. localhost:5000/query?funder.name=United States Agency
# i.e. localhost:5000/query?author.name=Herfort, Benjamin

@app.route('/query', methods=['GET'])
def api_query_by_field():
    search_value = ''
    search_field = ''

    for key in request.args:
        search_field = key
        search_value = request.args[key]

    result = es.search(index=index_name,
                       body={'query': {'match_phrase': {search_field: search_value}}})
    return jsonify(result)

if __name__ == '__main__':
    app.run()

