# -*- coding: utf-8 -*-
from django.db import models
from taggit.managers import TaggableManager


class PublicManager(models.Manager):
    def get_query_set(self):
        return super(PublicManager, self).get_query_set().filter(public='True').order_by('-created')


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField()
    tags = TaggableManager(blank=True)
    public = models.BooleanField(default=True)
    objects = models.Manager()
    publics = PublicManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/blog/%i' % self.id


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads')
    url = models.CharField(max_length=200)
    priority = models.IntegerField(max_length=100, default=0)

    def get_absolute_url(self):
        return '/projects/%i' % self.id

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['priority', 'name']
        verbose_name = 'Проект'
        verbose_name_plural = 'проекты'
