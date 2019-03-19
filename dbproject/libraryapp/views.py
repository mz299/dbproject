# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from libraryapp.forms import RegistrationForm
import datetime
import calendar

# Create your views here.

def home(request):
    user = request.user

    if not request.user.is_authenticated():
        return redirect('/libraryapp/login/')
    
    data = []
    copys = Copy.objects.all()
    for copy in copys:
        d = {'copy': copy}
        authors = []
        for write in copy.doc.book.writes_set.all():
            authors.append(write.author.name)
        authors = ', '.join(authors)
        d.update({'author': authors})
        for bor in copy.bortransaction_set.all():
            d.update({'borrowed': True})
        data.append(d)
        
    args = {'user': request.user,
            'data': data}

    return render(request, 'libraryapp/home.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/libraryapp/')
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'libraryapp/register.html', args)

def profile(request):
    user = request.user
    if not request.user.is_authenticated():
        return redirect('/libraryapp/login/')
    args = {
        'user':request.user,
    }
    return render(request, 'libraryapp/profile.html', args)

def borrow(request, copy_id):
    copy = get_object_or_404(Copy, pk=copy_id)
    reader = request.user.reader

    if len(copy.bortransaction_set.all()) > 0:
        args = {'success': False, 'copy': copy,
                'reason': 'Ops, seems like somebody has already borrowed this book'}
        return render(request, 'libraryapp/borrow.html', args)

    if len(reader.bortransaction_set.all()) >= 3:
        args = {'success': False, 'copy': copy,
                'reason': 'You cannot borrow more than 3 books.'}
        return render(request, 'libraryapp/borrow.html', args)

    def add_months(sourcedate, months):
        month = sourcedate.month - 1 + months
        year = int(sourcedate.year + month / 12)
        month = month % 12 + 1
        day = min(sourcedate.day, calendar.monthrange(year, month)[1])
        return datetime.date(year, month, day)

    bor = borTransaction()
    bor.borDateTime = datetime.datetime.now()
    bor.dueDate = add_months(bor.borDateTime, 1)
    bor.reader = reader
    bor.copy = copy
    bor.save()

    args = {'success': True, 'copy': copy}
    return render(request, 'libraryapp/borrow.html', args)

def mybook(request):
    bor = borTransaction.objects.filter(reader=request.user.reader)
    for b in bor:
        b.reader
    args = {'bor': bor}
    return render(request, 'libraryapp/mybook.html', args)

def retbook(request, bor_id):
    bor = get_object_or_404(borTransaction, pk=bor_id)
    if bor.reader != request.user.reader:
        args = {'message': 'You are tring to return a wrong book'}
        return render(request, 'libraryapp/return.html', args)

    bor.delete()

    args = {'message': 'Return success!'}
    return render(request, 'libraryapp/return.html', args)

def search(request):
    keyword = request.POST['keyword']

    data = []
    copys = Copy.objects.filter(doc__title__icontains=keyword)
    for copy in copys:
        d = {'copy': copy}
        authors = []
        for write in copy.doc.book.writes_set.all():
            authors.append(write.author.name)
        authors = ', '.join(authors)
        d.update({'author': authors})
        for bor in copy.bortransaction_set.all():
            d.update({'borrowed': True})
        data.append(d)

    args = {'user': request.user,
            'data': data,
            'keyword': keyword}

    return render(request, 'libraryapp/search.html', args)


