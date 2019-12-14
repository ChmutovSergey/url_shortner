from django.db import models


# Create your models here.
class Urls(models.Model):

    md_url = models.CharField(max_length=32, primary_key=True)
    short_url = models.SlugField(max_length=6)
    http_url = models.URLField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.http_url
