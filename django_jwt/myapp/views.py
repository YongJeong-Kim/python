from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# Create your views here.
from .models import Post

# 아래 클래스와 동일
# @api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
# @authentication_classes((JSONWebTokenAuthentication,))
# def posts(request):
#     posts = Post.objects.filter(
#         published_at__isnull=False).order_by('-published_at')
#     post_list = serializers.serialize('json', posts)
#     return HttpResponse(post_list, content_type="text/json-comment-filtered")


class PostApiView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        posts = Post.objects.filter(
            published_at__isnull=False).order_by('-published_at')
        post_list = serializers.serialize('json', posts)
        return HttpResponse(post_list, content_type="text/json-comment-filtered")