from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status


@api_view(['GET', 'POST'])
def list_blog(request):
    if request.method == "GET":
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def detail_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(serializer.errors)
    
    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == "DELETE":
        blog.delete()
        return Response(serializer.errors)
