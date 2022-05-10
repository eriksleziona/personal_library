from django.shortcuts import render
from django.views.generic import ListView
from .models import Book


# Create your views here.

class HomeView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'books/home.html'
