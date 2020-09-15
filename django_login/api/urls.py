from django.urls import path

from api.views import SigninView, TestView, SignoutView, SignupView

app_name = 'login'
urlpatterns = [
    path('login/', SigninView.as_view()),
    path('logout/', SignoutView.as_view()),
    path('signup/', SignupView.as_view()),
    path('test/', TestView.as_view()),
]
