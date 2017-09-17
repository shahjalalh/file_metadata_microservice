from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FileUpload(models.Model):
    datafile = models.FileField(upload_to='media/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.datafile.name
