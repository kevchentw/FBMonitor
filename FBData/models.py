from django.db import models
import django.utils
class FBData(models.Model):
    page_id = models.IntegerField()
    post_id = models.IntegerField()
    comments = models.IntegerField()
    likes = models.IntegerField()
    shares = models.IntegerField()
    time = models.DateTimeField()
    created = models.DateTimeField(default=django.utils.timezone.now)
