#from django.db import models

# Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User 		# 추가

class Bookmark(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 	 	# 추가	

    def __str__(self):
        return self.title
