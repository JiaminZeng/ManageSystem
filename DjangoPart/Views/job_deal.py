from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class JobTypeUpdate(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']

        mc = request.data['mc']
        new_mc = request.data['new_mc']
        tp = request.data['type']

        user = get_username(token)
        ret = {'code': -1}
        users = models.User_2.objects.filter(username=user)
        if users.exists():
            cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if tp == 1:
                models.JobType.objects.create(mc=new_mc, sj=cur_time)
            elif tp == 2:
                t = models.JobType.objects.filter(mc=mc)
                t.update(mc=new_mc, sj=cur_time)
            else:
                t = models.JobType.objects.filter(mc=mc)
                t.delete()
            ret['code'] = 1
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class JobTypeGet(APIView):
    def post(self, request, *args, **kwargs):
        ret = []
        types = models.JobType.objects.all()
        for item in types:
            tp = model_to_dict(item)
            tp['new_mc'] = tp['mc']
            ret.append(tp)

        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class JobUpdate(APIView):
    def post(self, request, *args, **kwargs):
        token = request.data['token']
        tp = request.data['type']
        user = get_username(token)
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        users = models.User_1.objects.filter(username=user)
        if not users.exists():
            users = models.User_2.objects.filter(username=user)
        ret = {'code': -1}
        if users.exists():
            if tp == 1:
                data = request.data['data']
                data['fbsj'] = cur_time
                data['fbzyhm'] = user
                user = model_to_dict(users[0])
                data['fbz'] = user['username']
                data['lxdh'] = user['dh']
                data['jgdm'] = user['jgdm']
                data['zt'] = 1
                models.Job.objects.create(**data)
            elif tp == 2:
                data = request.data['data']
                t = models.Job.objects.filter(id=data['id'])
                data.pop("qymc")
                data.pop("qydz")
                data.pop("qyxz")
                data.pop("zyyw")
                data.pop("djsj")
                t.update(**data)
            elif tp == 0:
                id = request.data['id']
                t = models.Job.objects.filter(id=id)
                t.delete()
                t = models.Resume.objects.filter(zwid=id)
                t.delete()
            elif tp == 4:
                id = request.data['id']
                t = models.Job.objects.filter(id=id)
                t.update(zt=0)
            elif tp == 5:
                id = request.data['id']
                t = models.Job.objects.filter(id=id)
                t.update(zt=1)
            ret['code'] = 1

        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'

        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response


class JobGet(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        tp = data['type']
        ret = []
        if 'token' in data.keys():
            fbz = get_username(data['token'])
            jobs = models.Job.objects.filter(zt=tp, fbz=fbz)
        elif 'zwlb' in data.keys() and data['zwlb'] != 'ALL':
            jobs = models.Job.objects.filter(zt=tp, zwlb=data['zwlb'])
        else:
            jobs = models.Job.objects.filter(zt=tp)
        for item in jobs:
            tp = model_to_dict(item)
            company = models.Company.objects.filter(jgdm=tp['jgdm'])[0]
            company = model_to_dict(company)
            tp['qymc'] = company['qymc']
            tp['qydz'] = company['qydz']
            tp['qyxz'] = company['qyxz']
            tp['zyyw'] = company['zyyw']
            tp['djsj'] = company['djsj']
            ret.append(tp)

        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response
