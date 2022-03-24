from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        data["zhzt"] = 1
        user = request.data["username"]
        result = models.User_0.objects.filter(username=user)

        ret = {
            'code': 1,
            'username': user,
        }
        if result.exists():
            ret['code'] = -1
        else:
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            data['zcsj'] = cur_time
            ret['username'] = user
            models.User_0.objects.create(**data)

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class GetInformation(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        ret = models.User_0.objects.filter(username=user)[0]
        ret = model_to_dict(ret)
        ret["password"] = ''
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class UpdateInformation(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data['dataList']
        new_password = request.data['new_password']
        user = data['username']
        pd = data['password']
        result = models.User_0.objects.filter(username=user, password=pd)
        ret = {'code': 0}
        if result.exists():
            if new_password != '':
                data['password'] = new_password
            result.update(**data)
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


class RegisterView_C0(APIView):

    def post(self, request, *args, **kwargs):

        user = request.data["user"]
        company = request.data["company"]

        username = user["username"]
        jgdm = company["jgdm"]

        result_0 = models.User_0.objects.filter(username=username)
        result_1 = models.User_1.objects.filter(username=username)
        result_2 = models.User_2.objects.filter(username=username)
        result_3 = models.Company.objects.filter(jgdm=jgdm)

        ret = {
            'code': 1,
        }
        if result_0.exists() or result_1.exists() or result_2.exists() or result_3.exists():
            ret['code'] = -1
        else:
            user["yhjb"] = 1
            user["zhzt"] = 0
            user["jgdm"] = jgdm
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            user['zcsj'] = cur_time
            models.User_1.objects.create(**user)
            company['djsj'] = cur_time
            company["fzzh"] = username
            models.Company.objects.create(**company)

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class RegisterView_C1(APIView):

    def post(self, request, *args, **kwargs):

        data = request.data
        user = data['user']
        qymc = data['qymc']
        jgdm = data['jgdm']

        username = user['username']
        result_0 = models.User_0.objects.filter(username=username)
        result_1 = models.User_1.objects.filter(username=username)
        result_2 = models.User_2.objects.filter(username=username)

        result_ = models.Company.objects.filter(qymc=qymc, jgdm=jgdm)
        ret = {
            'code': 1,
            'username': user,
        }
        if result_0.exists() or result_1.exists() or result_2.exists():
            ret['code'] = -1
        elif result_.exists():
            user['zhzt'] = 0
            user['yhjb'] = 2
            user['jgdm'] = jgdm
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            user['zcsj'] = cur_time
            models.User_1.objects.create(**user)
        else:
            ret['code'] = 0
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class GetInformation_C(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        user = get_username(token)
        user = models.User_1.objects.filter(username=user)
        if not user.exists():
            user = models.User_2.objects.filter(username=user)
        user = user[0]

        user = model_to_dict(user)
        user['password'] = ''
        jgdm = user['jgdm']
        user['password'] = ''

        company = models.Company.objects.filter(jgdm=jgdm)[0]
        company = model_to_dict(company)
        ret = {'user': user, 'company': company}
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class UpdateInformation_C(APIView):
    def post(self, request, *args, **kwargs):
        user = request.data['user']
        company = request.data['company']

        new_password = request.data['new_password']
        username = user['username']
        password = user['password']

        jgdm = company['jgdm']

        result = models.User_1.objects.filter(username=username, password=password)
        if not result.exists():
            result = models.User_2.objects.filter(username=username, password=password)

        ret = {'code': 0}
        if result.exists():
            if new_password != '':
                user['password'] = new_password
            result.update(**user)
            result = models.Company.objects.filter(jgdm=jgdm)
            result.update(**company)
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
