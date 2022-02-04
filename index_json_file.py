# load and index the json file in Elasticsearch
# Qin Zhang 02/03/2022

from elasticsearch import Elasticsearch
import json

es = Elasticsearch()

index_name = 'myindex'
type_name = 'mydataset'

# checking if the index exists

if es.indices.exists(index=index_name):

    # Delete index

    es.indices.delete(index=index_name)
else:

    # Creating index

    es.indices.create(index=index_name)


def load_json_index():
    json_file = 'harvard_dataverse.json'
    with open(json_file) as f:
        myobjects = json.load(f)
        for item in myobjects:
            id = item['@id'] # select @id as id to load data to ES
            resp = es.index(index=index_name, doc_type=type_name,
                            ignore=400, id=id, body=item)


if __name__ == '__main__':
    load_json_index()

