from django.urls import path

from api.views import RedisTestView

urlpatterns = [
    path('', RedisTestView.as_view())
]