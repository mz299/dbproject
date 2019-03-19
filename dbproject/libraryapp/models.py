# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reader(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=500, default='')
    phone = models.CharField(max_length=15, default='')
    readerType = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.user)

class Branch(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default='')
    location = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

class Publisher(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name

class Document(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=300, default='')
    date = models.DateField()
    descriptor = models.CharField(max_length=300, default='')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Copy(models.Model):
    objects = models.Manager()
    position = models.CharField(max_length=300, default='')
    lib = models.ForeignKey(Branch, on_delete=models.CASCADE)
    doc = models.ForeignKey(Document, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.doc) + "-" + str(self.lib) + "-" + self.position 

class Reservation(models.Model):
    objects = models.Manager()
    resDateTime = models.DateTimeField()
    resStatus = models.CharField(max_length=300, default='')
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    reader = models.ForeignKey(Reader)

    def __str__(self):
        return str(self.reader) + "-" + str(self.copy)

    class Meta:
        unique_together = ('copy', 'reader')

class borTransaction(models.Model):
    objects = models.Manager()
    borDateTime = models.DateTimeField()
    dueDate = models.DateField()
    retDate = models.DateField(null=True)
    fineAmount = models.FloatField(default=0)
    reader = models.ForeignKey(Reader)
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.reader) + "-" + str(self.copy)

    class Meta:
        unique_together = ('copy', 'reader')

class Author(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class Book(models.Model):
    objects = models.Manager()
    doc = models.OneToOneField(Document, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=100, default='', unique=True)

    def __str__(self):
        return str(self.doc)

class Writes(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(Author)
    book = models.ForeignKey(Book)

    def __str__(self):
        return str(self.book) + ' - ' + str(self.author)

    class Meta:
        unique_together = ('author', 'book')

class Proceeding(models.Model):
    objects = models.Manager()
    doc = models.OneToOneField(Document, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=500, default='')
    editor = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.doc)

class ChiefEditor(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name

class JournalVolume(models.Model):
    objects = models.Manager()
    doc = models.OneToOneField(Document, on_delete=models.CASCADE)
    volumeNo = models.IntegerField(default=0)
    editorId = models.ForeignKey(ChiefEditor)

    def __str__(self):
        return str(self.doc)

class JournalIssue(models.Model):
    objects = models.Manager()
    vol = models.ForeignKey(JournalVolume, on_delete=models.CASCADE)
    Scope = models.CharField(max_length=100, default='')
    editor = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.volId)
