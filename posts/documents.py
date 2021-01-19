from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry


from .models import Post

@registry.register_document
class PostDocument(Document):
    class Index:
        '''
        Elasticsearch index
        '''
        name='posts'
    url = fields.TextField(attr='get_absolute_url')
    score = fields.FloatField(attr='elastic_score')
    class Django:
        model = Post
        fields = [
            'id',
            'title',
            'content'
        ]