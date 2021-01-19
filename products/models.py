from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)

    def get_absolute_url(self):
        return f"products/{self.id}"
    
    @property
    def elastic_score(self):
        return 0.95