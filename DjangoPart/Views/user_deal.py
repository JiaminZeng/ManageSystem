from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class UserGet(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        ret = models.User_1.objects.filter(username=user)[0]
        ret = model_to_dict(ret)
        jgdm = ret['jgdm']
        yhjb = ret['yhjb']
        ret = []
        if yhjb == 1:
            users = models.User_1.objects.filter(jgdm=jgdm, zhzt=0)
            for item in users:
                user = model_to_dict(item)
                user['password'] = ''
                ret.append(user)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class CompanyGet(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        ret = models.User_2.objects.filter(username=user)
        if ret.exists():
            ret = []
            users = models.User_1.objects.filter(yhjb=1, zhzt=0)
            for item in users:
                user = model_to_dict(item)
                company = models.Company.objects.filter(jgdm=user['jgdm'])[0]
                company = model_to_dict(company)
                user['password'] = ''
                user['qymc'] = company['qymc']
                user['qydz'] = company['qydz']
                user['qyxz'] = company['qyxz']
                user['zyyw'] = company['zyyw']
                ret.append(user)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class NormalGet(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        cur = models.User_2.objects.filter(username=user)
        ret = []
        if cur.exists():
            users = models.User_0.objects.filter(zhzt=1)
            for item in users:
                user = model_to_dict(item)
                user['password'] = ''
                user['yhlx'] = '普通用户'
                ret.append(user)
            users = models.User_1.objects.filter(zhzt=1)
            for item in users:
                user = model_to_dict(item)
                user['password'] = ''
                if user['yhjb'] == 1:
                    user['yhlx'] = '企业管理用户'
                else:
                    user['yhlx'] = '企业一般用户'
                ret.append(user)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class FreezeGet(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        cur = models.User_2.objects.filter(username=user)
        ret = []
        if cur.exists():
            users = models.User_0.objects.filter(zhzt=-1)
            for item in users:
                user = model_to_dict(item)
                user['password'] = ''
                user['yhlx'] = '普通用户'
                ret.append(user)
            users = models.User_1.objects.filter(zhzt=-1)
            for item in users:
                user = model_to_dict(item)
                user['password'] = ''
                if user['yhjb'] == 1:
                    user['yhlx'] = '企业管理用户'
                else:
                    user['yhlx'] = '企业一般用户'
                ret.append(user)
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class StsteUpdate(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        username = request.data['username']
        tp = request.data['type']

        user = get_username(token)
        cur = models.User_1.objects.filter(username=user)
        if not cur.exists():
            cur = models.User_2.objects.filter(username=user)

        ret = {'code': -1}
        users = models.User_1.objects.filter(username=username)
        if not users.exists():
            users = models.User_0.objects.filter(username=username)
        if users.exists() and cur.exists():
            if tp == 1:
                users.update(zhzt=1)
            elif tp == 0:
                users.delete()
            elif tp == -1:
                users.update(zhzt=-1)
            ret['code'] = 1

        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response
