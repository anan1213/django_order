from django.db import models
from django.utils import timezone
# Create your models here.

class SubClass(models.Model):
    subclass = models.CharField("クラスタリングのタイトル", max_length=20)
    created_at = models.DateTimeField('日付', auto_now= True)
    def __str__(self):
        return self.subclass



class Url(models.Model):
    site = models.TextField("URL", max_length=140)
    site_name = models.CharField('URLの説明', max_length=20)
    subclass = models.ForeignKey(
      SubClass, verbose_name='タイトルの名前', on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField('日付', auto_now=True)

    def __str__(self):
        return self.site_name
