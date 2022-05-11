from django.urls import path
from .views import HomeView, AddBookView, BookDetailView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/', AddBookView.as_view(), name='add'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(), name='detail')
]
