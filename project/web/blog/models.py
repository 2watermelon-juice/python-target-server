# from django.db import models
# Create your models here.

from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

from tagging.fields import TagField
from django.utils.encoding import force_str
from django.contrib.auth.models import User	# 추가
from django.utils.text import slugify		# 추가

# create your models here.

class Post(models.Model):
    title = models.CharField('TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date', auto_now_add=True)
    modify_date = models.DateTimeField('Modify Date', auto_now=True)
    tag = TagField()
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 	# 추가

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'my_post'
        ordering = ('-modify_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()

    def save(self, *args, **kwargs):					# 추가
        if not self.id:							# 추가
            self.slug = slugify(self.title, allow_unicode=True)		# 추가
        super(Post, self).save(*args, **kwargs)				# 추가 
