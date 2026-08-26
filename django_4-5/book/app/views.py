from django.shortcuts import render,redirect
from .models import Book,Readership
from .forms import BookForm,ReaderModelship

def home(request):
    return render(request,'home.html')

def about(request):
    books = Book.objects.all()

    return render(request,'about.html', {'books': books})

def book(request):
    if request.method =='POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book_title = form.cleaned_data['title']
            book_language = form.cleaned_data['language']
            book_type = form.cleaned_data['type']
            book_comment = form.cleaned_data['comment']

            Book.objects.create(title=book_title,language=book_language,
                                type = book_type,comment = book_comment)
            return redirect ('book')
    else:
        form = BookForm()
        books = Book.objects.all()
        context = {
            'form':form,
            'books':books
            }
    return render(request,'books.html',context)

def reader(request):
    if request.method =='POST':
        form = ReaderModelship(request.POST)
        if form.is_valid():
             form.save()
             return redirect('reader')
    else:
             form = ReaderModelship()
    readers = Readership.objects.all()
    context = {
             'form':form,
             'readers':readers
        }
    return render(request,'reader.html',context)


                   