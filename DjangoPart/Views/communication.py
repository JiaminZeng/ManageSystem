from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class LinkCreate(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        token = data['token']
        user0 = get_username(token)
        user1 = data['user1']
        result = models.Link.objects.filter(user0=user0, user1=user1)
        if result.exists():
            result.delete()
        models.Link.objects.create(user0=user0, user1=user1)
        ret = {'code': 1}
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class LinkGet(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        token = data['token']
        user = get_username(token)
        tp = data['type']
        ret = []
        if tp == 1:
            links = models.Link.objects.filter(user0=user)
            for item in links:
                item = model_to_dict(item)
                ret.append(item['user1'])
        else:
            links = models.Link.objects.filter(user1=user)
            for item in links:
                item = model_to_dict(item)
                ret.append(item['user0'])
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class MessageGet(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        tp = data['type']
        token = data['token']
        user = get_username(token)

        if tp == 1:
            user1 = data['user']
            result = models.Message.objects.filter(user0=user, user1=user1)
        else:
            user0 = data['user']
            result = models.Message.objects.filter(user0=user0, user1=user)

        ret = []
        for item in result:
            item = model_to_dict(item)
            if str(item['sender']) == str(user):
                item['sender'] = 1
            else:
                item['sender'] = 2
            ret.append(item)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class MessageCreate(APIView):

    def post(self, request, *args, **kwargs):
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        data = request.data
        tp = data['type']
        token = data['token']
        user = get_username(token)
        content = data['content']

        if tp == 1:
            user1 = data['user']
            models.Message.objects.create(user0=user, user1=user1, time=cur_time, content=content, sender=user)
        else:
            user0 = data['user']
            models.Message.objects.create(user0=user0, user1=user, time=cur_time, content=content, sender=user)

        ret = {'code': 1}
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response
