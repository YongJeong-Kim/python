from django.core import cache
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class RedisTestView(View):
    def get(self, request):
        cache.set('test', 'test value')
        return cache.get('test')