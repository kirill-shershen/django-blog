from django.db import models
from taggit.managers import TaggableManager

class PublicManager(models.Manager):
    def get_query_set(self):
        return super(PublicManager, self).get_query_set().filter(public='True').order_by('-created')

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager()
    public= models.BooleanField(default=True)
    objects = models.Manager()
    publics = PublicManager()

    def __unicode__(self):
        return self.title