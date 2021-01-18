# query elasticsearch
from django.conf import settings
import elasticsearch
from elasticsearch_dsl import Search

ELASTIC_HOST_KEY = getattr(settings, 'ELASTIC_HOST_KEY')

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST_KEY])

INDEXES = [
    'posts',
    'products'
]


def perform_lookup(query, index=INDEXES, fields = ['title', 'content']):
    if not query:
        return
    search_results = Search(
        index=index).using(client).query("multi_match", 
        fields=fields,  fuzziness='AUTO', query=query)
    results = []
    for hit in search_results:
        print(hit.id)
        print(hit.title)
        print(hit.meta.index)
        print(hit.meta.score)
        data = {
            "id": hit.id,
            "title": hit.title,
            "index": hit.meta.index,
            "content": hit.content,
            "url": hit.url,
        }
        results.append(data)
    return results