from django.shortcuts import render
from django.http import JsonResponse

def list(request):
    data = {
        "message": "This is the list view."
    }
    return JsonResponse(data)

def create(request):
    pass

#serializer = BookSerializer(data=request.data)