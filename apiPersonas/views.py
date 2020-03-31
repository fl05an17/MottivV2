from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Persona
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from rest_framework.authtoken.models import Token
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.permissions import IsAuthenticated
from .serializers import PersonaSerializer
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import status



# lista basda en clase (lo que hace es crear una instancia del modelo Usuario)
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()  # Consulta para indicarle que datos traer
    serializer_class = PersonaSerializer  # le indica a Django Rest framework que modelo serializado se va utilizar
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication, SessionAuthentication]


class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('apiPersonas:persona_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(
                self.get_success_url())  # Es un metodo que me permite redireccionar la url donde le haya indicado en
            # el parametro de arriba
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        token, _ = Token.objects.get_or_create(user=user)
        if token:
            login(self.request, form.get_user())
            return super(Login, self).form_valid(form)


class Logout(APIView):
    def get(self, request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=status.HTTP_200_OK)
