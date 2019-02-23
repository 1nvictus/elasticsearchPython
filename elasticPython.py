
import requests
res = requests.get('http://localhost:9200')
print(res.content)
#connect to our cluster
from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#index some test data
text='Anuj is my name'
print(es.index(index='test-index', doc_type='test', id=1, body={'test': text}))
print("done")
