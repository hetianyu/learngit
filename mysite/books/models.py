from django.db import models

class Author(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.CharField(max_length=50,)
    AuthorID = models.CharField(max_length=50,primary_key=True)
    Country = models.CharField(max_length=50)
class Book(models.Model):
    ISBN = models.CharField(max_length=50,primary_key=True)
    Price =  models.CharField(max_length=50)
    Publishdate = models.DateField()
    Publisher = models.CharField(max_length=50)
    Title = models.CharField(max_length=50)
    AuthorID = models.ForeignKey(Author)
    


