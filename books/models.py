from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
'''
Author
    name 
    birth_date 
    biography 

Book
    title 
    author 
    publication_date 
    price 

Review:
    book 
    reviewer_name
    content 
    rating(1:5)  
----------------------------  
ToDo:
    - github repo with project 
    - design models 
    - Generate CRUD for Books
'''


class Book(models.Model):
    title = models.CharField(max_length=100)
    publish_date= models.DateTimeField(default=timezone.now)
    price=models.IntegerField()
    author = models.ForeignKey(User,related_name='book_author',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title



class author(models.Model):
    name = models.ForeignKey(User,related_name='author_name',on_delete=models.CASCADE)
    biography = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    

class review(models.Model):
    pass
    