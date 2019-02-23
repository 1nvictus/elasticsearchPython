from tika import parser

file = '/home/fractaluser/Downloads/test.pdf'
# Parse data from file
file_data = parser.from_file(file)
# Get files text content
text = file_data['content']
print(text)


import requests
res = requests.get('http://localhost:9200')
print(res.content)
#connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#index some test data
print(es.index(index='tika-index', doc_type='textcontent', id=5, body={'content': text}))
print("done")
