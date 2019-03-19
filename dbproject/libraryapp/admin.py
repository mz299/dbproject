# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from libraryapp.models import *

admin.site.register(Reader)
admin.site.register(Branch)
admin.site.register(Publisher)
admin.site.register(Document)
admin.site.register(Copy)
admin.site.register(Reservation)
admin.site.register(borTransaction)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Writes)
admin.site.register(Proceeding)
admin.site.register(ChiefEditor)
admin.site.register(JournalVolume)
admin.site.register(JournalIssue)
