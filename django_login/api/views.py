from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic.base import View

from api.forms import LoginForm


class SigninView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(SigninView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        form = LoginForm(request.POST)
        id = request.POST['username']
        password = request.POST['password']
        u = authenticate(username=id, password=password)

        if u:
            login(request, user=u)
            response = {'success': True}
            return JsonResponse(response, status=200)
        else:
            response = {'success': False}
            return JsonResponse(response, status=400)


class SignupView(View):
    def post(self, request):
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            username = request.POST['username']
            email = request.POST['email']
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=username, email=email, password=password1, is_staff=True)
                response = {'success': True}
                return JsonResponse(response, status=201)
            else:
                response = {'success': False, 'message': '이미 존재하는 username입니다.'}
                return JsonResponse(response, status=201)
        else:
            response = {'success': False, 'message': '서로 비밀번호가 다릅니다.'}
            return JsonResponse(response, status=400)


class SignoutView(View):
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(SignoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        logout(request)
        response = {'success': True}
        return JsonResponse(response, status=200)


@method_decorator(login_required, name='dispatch')
class TestView(View):
    def get(self, request):
        response = {'data': 'test data'}
        return JsonResponse(response, status=200)