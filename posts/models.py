from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    single blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30)
    image = models.ImageField(upload_to='img', null=True, blank=True) #this img is the one in the root folder (media/img)

    def __unicode__(self):
        return self.title