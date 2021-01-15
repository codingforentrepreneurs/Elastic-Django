import elasticsearch
from elasticsearch_dsl import Search
import pathlib

ELASTIC_INDEX_NAME = 'cfe-posts-2'
ELASTIC_PORT = 9231
ELASTIC_HOST = f'http://localhost:{ELASTIC_PORT}'

client = elasticsearch.Elasticsearch(hosts=[ELASTIC_HOST])

post_1 = {
    "id": 1,
    "title": "This is awesome",
    "content": "Here is my data about Django."
}

post_2 = {
    "id": 2,
    "title": "Telsa is crushing self driving",
    "content": "Maybe"
}

post_3 = {
    "id": 2,
    "title": "Install guide",
    "content": pathlib.Path("install_elasticsearch.md").read_text()
}

# client.index(index=ELASTIC_INDEX_NAME, body=post_1)

# client.index(index=ELASTIC_INDEX_NAME, body=post_2)

# client.index(index=ELASTIC_INDEX_NAME, body=post_3)


if __name__ == "__main__":
    user_query = input("What are you looking for?\n")
    fields = ['title', 'content']
    results = Search(
        index=ELASTIC_INDEX_NAME).using(client).query("multi_match", 
        fields=fields,  fuzziness='AUTO', query=user_query)
    for hit in results:
        print(hit.id)
        print(hit.title)