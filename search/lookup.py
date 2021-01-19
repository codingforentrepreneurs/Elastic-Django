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


def perform_lookup(query, index=INDEXES, fields = ['title', 'content'], internal_sort=True):
    if not query:
        return
    search_results = Search(
        index=index).using(client).query("multi_match", 
        fields=fields,  fuzziness='AUTO', query=query)
    results = []
    for hit in search_results:
        elasticsearch_score = hit.meta.score
        hit_score = hit.score
        data = {
            "id": hit.id,
            "title": hit.title,
            "index": hit.meta.index,
            "content": hit.content,
            "score": elasticsearch_score * hit_score,
            "url": hit.url,
        }
        print(data)
        results.append(data)
    if internal_sort:
        results = sorted(results, key=lambda x: x['score'], reverse=True)
    return results