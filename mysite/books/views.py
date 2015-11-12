from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context
from books.models import Book,Author
def index(request):
    book_list=Book.objects.all()
    c=Context({"book_list":book_list})
    return render_to_response("index.html",c)
def addbook(request):
    if request.POST:
        post=request.POST
        a=Author(AuthorID=post['AID'],Name=post['AN'],Age=post['AA'],Country=post['AC'])
        a.save()
        b=Book(ISBN=post['BI'],Price=post['BP'],Publishdate=post['BPD'],Publisher=post['BPE'],Title=post['BT'],AuthorID=a)
        b.save()
    return HttpResponseRedirect("/home/")
def add(request):
    return render_to_response("add.html")

def search(request):
    DouB=request.GET['searchname']
    Author_list=Author.objects.filter(Name=DouB)
    book_list=[]
    for auth in Author_list:
        book_list.extend(Book.objects.filter(AuthorID=auth))
    c=Context({"book_list":book_list})
    return render_to_response("search.html",c)
def information(request):
    bookid = request.GET['ID']
    Infor = Book.objects.get(ISBN = bookid)
    c = Context({'Book':Infor})
    return render_to_response("information.html", c)
def delete(request):
    bookid = request.GET['ID']
    Book.objects.get(ISBN = bookid).delete()
    return HttpResponseRedirect("/home/")


            

