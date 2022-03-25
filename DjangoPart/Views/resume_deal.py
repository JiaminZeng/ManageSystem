from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class ResumeUpdate(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        token = data['token']

        tp = data['type']
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        user = get_username(token)
        ret = {'code': -1}
        users = models.User_0.objects.filter(username=user)
        if not users.exists():
            users = models.User_1.objects.filter(username=user)
        if users.exists():
            if tp == 1:
                f = models.Resume.objects.filter(zwid=data['id'], tdz=user)
                if not f.exists():
                    models.Resume.objects.create(tdsj=cur_time, zt='已投递', hf='', zwid=data['id'], fbz=data['fbz'],
                                                 tdz=user)
                    ret['code'] = 1
            elif tp == 2:
                f = models.Resume.objects.filter(id=data['id'])
                f.update(zt=data['zt'], hf=data['hf'])
                ret['code'] = 1
            elif tp == 3:
                f = models.Resume.objects.filter(id=data['id'])
                f.delete()
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


class ResumeGet(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        tp = data['type']
        state = data['state']
        token = data['token']
        user = get_username(token)
        ret = []

        if tp == 1:
            yhf = []
            whf = []
            zwid = data['zwid']
            resumes = models.Resume.objects.filter(zt='已投递', fbz=user, zwid=zwid)
            for item in resumes:
                item = model_to_dict(item)
                xx = models.User_0.objects.filter(username=item['tdz'])[0]
                xx = model_to_dict(xx)
                xx['password'] = ' '
                xx['tdsj'] = item['tdsj']
                xx['id'] = item['id']
                xx['hf'] = ''
                xx['zwid'] = zwid
                whf.append(xx)
            resumes = models.Resume.objects.filter(zt='同意', fbz=user, zwid=zwid)
            for item in resumes:
                item = model_to_dict(item)
                xx = models.User_0.objects.filter(username=item['tdz'])[0]
                xx = model_to_dict(xx)
                xx['password'] = ' '
                xx['tdsj'] = item['tdsj']
                xx['zt'] = item['zt']
                xx['hf'] = item['hf']
                xx['zwid'] = zwid
                yhf.append(xx)
            resumes = models.Resume.objects.filter(zt='拒绝', fbz=user, zwid=zwid)
            for item in resumes:
                item = model_to_dict(item)
                xx = models.User_0.objects.filter(username=item['tdz'])[0]
                xx = model_to_dict(xx)
                xx['password'] = ' '
                xx['tdsj'] = item['tdsj']
                xx['zt'] = item['zt']
                xx['hf'] = item['hf']
                xx['zwid'] = zwid
                yhf.append(xx)
            ret = {'yhf': yhf, 'whf': whf}
            print(ret)
        elif tp == 2:
            if state == 1:
                resumes = models.Resume.objects.filter(zt='已投递', tdz=user)
                for item in resumes:
                    item = model_to_dict(item)
                    tp = models.Job.objects.filter(id=item['zwid'])[0]
                    tp = model_to_dict(tp)
                    company = models.Company.objects.filter(jgdm=tp['jgdm'])[0]
                    company = model_to_dict(company)
                    tp['tdsj'] = item['tdsj']
                    tp['qymc'] = company['qymc']
                    tp['qydz'] = company['qydz']
                    tp['qyxz'] = company['qyxz']
                    tp['zyyw'] = company['zyyw']
                    tp['djsj'] = company['djsj']
                    ret.append(tp)
            elif state == 2:
                resumes = models.Resume.objects.filter(zt='同意', tdz=user)
                for item in resumes:
                    item = model_to_dict(item)
                    tp = models.Job.objects.filter(id=item['zwid'])[0]
                    tp = model_to_dict(tp)
                    company = models.Company.objects.filter(jgdm=tp['jgdm'])[0]
                    company = model_to_dict(company)
                    tp['tdsj'] = item['tdsj']
                    tp['hf'] = item['hf']
                    tp['zt'] = item['zt']
                    tp['qymc'] = company['qymc']
                    tp['qydz'] = company['qydz']
                    tp['qyxz'] = company['qyxz']
                    tp['zyyw'] = company['zyyw']
                    tp['djsj'] = company['djsj']
                    ret.append(tp)
                resumes = models.Resume.objects.filter(zt='拒绝', tdz=user)
                for item in resumes:
                    item = model_to_dict(item)
                    tp = models.Job.objects.filter(id=item['zwid'])[0]
                    tp = model_to_dict(tp)
                    company = models.Company.objects.filter(jgdm=tp['jgdm'])[0]
                    company = model_to_dict(company)
                    tp['tdsj'] = item['tdsj']
                    tp['hf'] = item['hf']
                    tp['zt'] = item['zt']
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
