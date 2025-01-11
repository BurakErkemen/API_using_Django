from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.book, name='book'),
    path('list/',views.book_list, name='book-list'),
    path('create/',views.book_create, name='book-create'),
]