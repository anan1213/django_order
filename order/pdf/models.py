from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Pdf(models.Model):
    title = models.CharField('タイトル', max_length=40)
    pdf = models.FileField('PDF', upload_to='uploads/%Y/%m/%d/', validators=[FileExtensionValidator(['pdf', ])], )

    def __str__(self):
        return self.title
