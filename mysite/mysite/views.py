from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from books.models import book,Author
def index(request):
    book_list=book.objects.all()
    c=Context({"book_list":book_list})
    return render_to_response("index.html",c)

