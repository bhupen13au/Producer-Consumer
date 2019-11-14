from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from producerapp.models import Books
from producerapp.serializer import BooksSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import HttpResponse

@csrf_exempt
def getUserToken(req):
    print('inside getusertoken')
    print(req.method)
    print('Username is -- ',req.POST['username'])
    #userin = User.objects.get(username=req.POST['username'])
    #token = Token.objects.create(user=userin)
    u = User.objects.get(username=req.POST['username'])
    key = Token.objects.get(user_id=u.id)
    print(key)
    return HttpResponse(key)


class BookOperations(ModelViewSet):
    permission_classes = (IsAuthenticated)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

