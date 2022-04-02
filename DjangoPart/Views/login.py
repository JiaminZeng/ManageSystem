from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        user = request.data["user_name"]
        pd = request.data["user_password"]

        ret = {
            'username': user,
            'type': -1,
            'token': 0,
            'yhjb': 2,
        }

        result_0 = models.User_0.objects.filter(username=user, password=pd, zhzt=1)
        result_1 = models.User_1.objects.filter(username=user, password=pd, zhzt=1)
        result_2 = models.User_2.objects.filter(username=user, password=pd)

        if result_0.exists():
            ret['token'] = create_token(user)
            ret['type'] = 1
        elif result_1.exists():
            c = result_1[0]
            c = model_to_dict(c)
            ret['yhjb'] = c['yhjb']
            ret['token'] = create_token(user)
            ret['type'] = 2
            print(ret)
        elif result_2.exists():
            ret['token'] = create_token(user)
            ret['type'] = 3

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response
