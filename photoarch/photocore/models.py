from django.db import models
from django.contrib.auth.models import User




# Create your models here.
class UploadFile(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=3, db_index=True)
    upload_time = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="files/%Y/%m/%d/", db_index=True)
    is_deleted = models.BooleanField(default=False)