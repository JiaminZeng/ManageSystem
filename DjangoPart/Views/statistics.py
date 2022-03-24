from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

from DjangoPart.tokens import *
from QZXT import models


class StatisticsGet(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        token = data['token']
        username = get_username(token)

        user = []
        zpxxsl = []
        jlsjsl = []
        result = models.User_1.objects.filter(username=username)[0]
        jgdm = model_to_dict(result)['jgdm']
        users = models.User_1.objects.filter(jgdm=jgdm)
        for item in users:
            item = model_to_dict(item)
            user.append(str(item['username']))
        for item in user:
            c = models.Job.objects.filter(fbz=item).count()
            zpxxsl.append(c)
            c = models.Resume.objects.filter(fbz=item).count()
            jlsjsl.append(c)

        hy = []
        zwgs = []
        jltd = []
        zdtd = []
        result = models.JobType.objects.all()
        for item in result:
            item = model_to_dict(item)
            hy.append(str(item['mc']))
        for item in hy:
            tot = models.Job.objects.filter(zwlb=item)
            c = tot.count()
            zwgs.append(c)
            mx = 0
            sum = 0
            for sub in tot:
                sub = model_to_dict(sub)
                id = sub['id']
                c = models.Resume.objects.filter(zwid=id).count()
                mx = max(mx, c)
                sum = sum + c
            jltd.append(sum)
            zdtd.append(mx)

        ret = {
            'user': user,
            'zpxxsl': zpxxsl,
            'jlsjsl': jlsjsl,
            'hy': hy,
            'zwgs': zwgs,
            'jltd': jltd,
            'zdtd': zdtd,
        }
        response = JsonResponse(ret, safe=False)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response

    def options(self, request, *args, **kwargs):
        response = HttpResponse()
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Headers'] = '*'
        return response
