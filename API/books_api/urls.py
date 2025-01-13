from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/',views.book, name='book'), # Retrieve-Update-Delete
    
    path('',views.books, name='books'), # Create-List
]