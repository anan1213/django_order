from django.db import models
from django.utils import timezone


class BookInfo(models.Model):
    title = models.CharField('タイトル', max_length=40)
    amazon_url = models.URLField('URL', max_length=1000)
    image_url = models.CharField('Imageurl', max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
