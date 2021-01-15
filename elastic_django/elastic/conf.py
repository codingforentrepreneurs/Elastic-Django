import os

ELASTICSEARCH_PORT = os.environ.get("ELASTICSEARCH_PORT", 9231)
ELASTIC_HOST_KEY = [f"http://localhost:{ELASTICSEARCH_PORT}"] # django 500

ELASTICSEARCH_DSL = {
    'default': {
        'hosts': [ELASTIC_HOST_KEY]
    }
}