# -*- coding: utf-8 -*-

from django.db import models


# Create your models here.
class Domain(models.Model):

    class Meta:
        db_table = 'tlds_domain'
    name = models.CharField(max_length=20, unique=True)
    lrm = models.BooleanField(default=True)
    label = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=30, blank=True)
    registry = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=30, blank=True)
    cate = models.CharField(max_length=30, blank=True)
    popular = models.IntegerField(blank=True)
    restrictions = models.CharField(max_length=200, blank=True)
    sources = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Registrar(models.Model):

    class Meta:
        db_table = 'tlds_registrar'
    keyword = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=50)
    review = models.TextField(blank=True)
    rating = models.FloatField(blank=True)

    def __str__(self):
        return self.name

class Price(models.Model):

    class Meta:
        db_table = 'tlds_price'
    name = models.ForeignKey(Domain)
    registrar = models.ForeignKey(Registrar)
    register = models.FloatField(blank=True)
    renewal = models.FloatField(blank=True)
    transfer = models.FloatField(blank=True)
    promo = models.FloatField(blank=True)
    privacy = models.FloatField(blank=True)


# Cheapest Price Table
class Cheapest(models.Model):

    class Mete:
        db_table = 'tlds_cheapest'
    name = models.CharField(max_length=20)
    updated = models.DateTimeField(blank=True)
    reg_registrar = models.CharField(max_length=30, blank=True)
    reg_price = models.FloatField(blank=True)
    renew_registrar = models.CharField(max_length=30, blank=True)
    renew_price = models.FloatField(blank=True)
    tran_registrar = models.CharField(max_length=30, blank=True)
    tran_price = models.FloatField(blank=True)
    popularity = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


# blog category


# blog tags


# blog post content
class Blog(models.Model):
    """
    blog content
    """
    title = models.CharField('title', max_length=100)
    author = models.CharField('author', max_length=16)
    slug = models.SlugField('slug', max_length=100, unique=True)
    content = models.TextField('content')
    created = models.DateTimeField('create_time', auto_now_add=True)
    category = models.CharField('category', max_length=50, blank=True)
    tags = models.CharField('tag', max_length=100, blank=True)

    def __str__(self):
        return self.title

# blog comment
class Comment(models.Model):
    """
    comment
    """
    blog = models.ForeignKey(Blog, verbose_name='blog')
    name = models.CharField('username', max_length=16)
    email = models.EmailField('email')
    content = models.TextField('content')
    created = models.DateTimeField('update_time', auto_now_add=True)

    def __str__(self):
        return self.content