# query elasticsearch
from django.conf import settings
import elasticsearch
from elasticsearch_dsl import Search

ELASTIC_HOST_KEY = getattr(settings, 'ELASTIC_HOST_KEY')

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST_KEY])


def perform_lookup(query, index='posts', fields = ['title', 'content']):
    if not query:
        return
    results = Search(
        index=index).using(client).query("multi_match", 
        fields=fields,  fuzziness='AUTO', query=query)
    for hit in results:
        print(hit.id)
        print(hit.title)