from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books_api.models import Book
from books_api.serializer import BookSerializer
from rest_framework import status


@api_view(['GET','POST'])
def books(request):
    if request.method == 'GET':
        books = Book.objects.all() # List all books
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data) # Create a new book
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def book(request,id):
    try:
       if request.method == 'GET':
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
       
       if request.method == 'PUT':
            book = Book.objects.get(pk=id)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
       if request.method == 'DELETE':
            book = Book.objects.get(pk=id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)                
    
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
