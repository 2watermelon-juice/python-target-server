from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from photo.fields import ThumbnailImageField

# create your models here.

class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))
        
class Photo(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
