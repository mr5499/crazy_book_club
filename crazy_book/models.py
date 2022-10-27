from django.db import models

# Create your models here.
class Book(models.Model):
    # book model
    name = models.CharField(max_length = 50) # the name of the book
    authors = models.JSONField() # author(s) of the book
    year_published = models.IntegerField() # year the book was published
    
    # the dates when the book was added and modified, both automatically maintained
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        # returns a string representation of the book's name
        return self.name

class Review(models.Model):
    # review model
    my_review = models.TextField() # the review of book(s)
    stars = models.IntegerField() # the star rating of a book
    unfinished = models.BooleanField() # tells if the book has been read or not
    
    # the dates when the review was added and modified, both automatically maintained
    date_added = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now_add = True)
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE) # foreign key of the book
    
    def __str__(self):
        # returns a string representation of the review in the reviews-part
        return f"{self.my_review[:50]}"