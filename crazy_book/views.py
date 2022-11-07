from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import BookForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def index(request):
    # the home page for crazy_book_club
    return render(request, 'crazy_book/index.html')

def books(request):
    # show all books
    books = Book.objects.order_by('date_added')
    context = {'books': books}
    return render(request, 'crazy_book/books.html', context)

def book(request, book_id):
    # show a single book and its reviews
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.all()
    context = {'book': book, 'reviews': reviews}
    return render(request, 'crazy_book/book.html', context)

@login_required
def new_book(request):
    # add a new book
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = BookForm()
    else:
        # POST data submitted; process data
        form = BookForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.owner = request.user
            new_review.save()
            return redirect('crazy_book:books')
        
    # display a blank or invalid form
    context = {'form': form}
    return render(request, 'crazy_book/new_book.html', context)

@login_required
def new_review(request, book_id):
    # add a new review for a book
    book = Book.objects.get(id=book_id)
    
    if request.method != 'POST':
        # no data submitted; create a blank form
        form = ReviewForm()
    else:
        # POST data submitted; process data
        form = ReviewForm(data=request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.book = book
            new_review.save()
            return redirect('crazy_book:book', book_id=book_id)
        
    # display a blank or invalid form
    context = {'book': book, 'form': form}
    return render(request, 'crazy_book/new_review.html', context)

@login_required
def edit_review(request, review_id):
    # edit an existing review
    review = Review.objects.get(id=review_id)
    book = review.book
    if book.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        # initial request; pre-fill form with the current book
        form = ReviewForm(instance=review)
    else:
        # POST data submitted; process data
        form = ReviewForm(instance=review, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('crazy_book:book', book_id=book.id)
    
    context = {'review': review, 'book': book, 'form': form}
    return render(request, 'crazy_book/edit_review.html', context)
        
        
        