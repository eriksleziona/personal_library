from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book


# Create your views here.

class HomeView(ListView):
    model = Book
    context_object_name = 'books_list'
    template_name = 'books/home.html'


class AddBookView(LoginRequiredMixin ,CreateView):
    model = Book
    fields = "__all__"
    success_url = reverse_lazy('home')


class BookDetailView(DetailView):
    model = Book

