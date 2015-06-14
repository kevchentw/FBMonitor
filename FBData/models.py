from django.db import models
from datetime import datetime

class FBData(models.Model):
    page_id = models.IntegerField()
    post_id = models.IntegerField()
    comments = models.IntegerField()
    likes = models.IntegerField()
    shares = models.IntegerField()
    time = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True, default=datetime.now())
