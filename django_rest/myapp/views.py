from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics, serializers
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Post
from .serializers import UserSerializer, PostSerializer


class UserViewSet(generics.ListAPIView):
    # queryset = User.objects.all().order_by('name')
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'page_size'

    def get(self, request):
        names = [user.name for user in User.objects.all()]
        return Response(list(User.objects.all().values()), status=200)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserDetailViewSet(generics.ListAPIView):
    def get(self, request, id):
        data = User.objects.get(pk=id)
        serializer = UserSerializer(data)
        return Response(serializer.data, status=200)

    def put(self, request, id):
        try:
            data = User.objects.get(pk=id)
            data.name = request.data.get('name')
            data.email = request.data.get('email')
            data.save()
            return Response(status=201)
        except User.DoesNotExist:
            return Response(status=404)

    def delete(self, request, id):
        try:
            data = User.objects.get(pk=id)
            data.delete()
            return Response(status=204)
        except User.DoesNotExist:
            return Response(status=404)


class PostViewSet(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        data = Post.objects.select_related('user')
        print(str(data.query))
        data2 = User.objects.prefetch_related('posts')
        print(str(data2.query))
        # aa = Post.objects.select_related('user')
        return Response(list(data.values), status=200)
