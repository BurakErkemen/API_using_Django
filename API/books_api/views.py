from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from books_api.models import Book
from books_api.serializer import BookSerializer
from rest_framework import status

@api_view(['GET'])
def book_list(request):
   books = Book.objects.all()
   serializer = BookSerializer(books, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def book(request,id):
    try:
        book = Book.objects.get(pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def book_create(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # This will save the validated data to the database
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
