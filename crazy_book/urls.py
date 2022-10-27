# defines URL patterns for learning_logs
from django.urls import path
from . import views

app_name = "crazy_book"
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # page that shows all the books
    path('books/', views.books, name='books'),
    # page for the book reviews
    path('books/<int:book_id>', views.book, name='book'),
    # page for adding a new book
    path('new_book/', views.new_book, name='new_book'),
    # page for adding a review
    path('new_review/<int:book_id>/', views.new_review, name='new_review'),
    # page for editing a review
    path('edit_review/<int:review_id>/', views.edit_review, name='edit_review'),
]
