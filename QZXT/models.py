from django.db import models


# Create your models here.
class User_0(models.Model):
    username = models.CharField(max_length=16, primary_key=True)  # 用户名
    password = models.CharField(max_length=16)  # 密码
    xm = models.CharField(max_length=16, null=True)  # 姓名
    xb = models.CharField(max_length=5, null=True)  # 性别
    mz = models.CharField(max_length=5, null=True)  # 民族
    jg = models.CharField(max_length=5, null=True)  # 籍贯
    nl = models.CharField(max_length=5, null=True)  # 年龄
    dh = models.CharField(max_length=13, null=True)  # 电话
    xx = models.CharField(max_length=32, null=True)  # 学校
    xl = models.CharField(max_length=32, null=True)  # 学历
    zy = models.CharField(max_length=32, null=True)  # 专业
    zwjs = models.CharField(max_length=200, null=True)  # 自我介绍
    gzjl = models.CharField(max_length=200, null=True)  # 工作经历
    jyjl = models.CharField(max_length=200, null=True)  # 教育经历
    hjjl = models.CharField(max_length=200, null=True)  # 获奖记录
    ahtc = models.CharField(max_length=200, null=True)  # 特长爱好
    qwxz = models.CharField(max_length=200, null=True)  # 期望薪资
    fjxx = models.CharField(max_length=200, null=True)  # 附加信息
    zcsj = models.CharField(max_length=50, null=True, default="-")  # 注册时间
    zhzt = models.IntegerField()  # 账号状态


class User_1(models.Model):
    username = models.CharField(max_length=16, primary_key=True)  # 用户名
    password = models.CharField(max_length=16)  # 密码
    yhjb = models.IntegerField()  # 用户级别
    jgdm = models.CharField(max_length=16)  # 机构代码
    xm = models.CharField(max_length=16)  # 姓名
    xb = models.CharField(max_length=16)  # 性别
    dh = models.CharField(max_length=16)  # 电话
    zw = models.CharField(max_length=16)  # 职位
    zcsj = models.CharField(max_length=50, null=True, default="-")  # 注册时间
    zhzt = models.IntegerField()  # 账号状态


class User_2(models.Model):
    username = models.CharField(max_length=16, primary_key=True)  # 用户名
    password = models.CharField(max_length=16)  # 密码


class Company(models.Model):
    jgdm = models.CharField(max_length=16, primary_key=True)  # 机构代码
    qymc = models.CharField(max_length=64)  # 企业名称
    fzzh = models.CharField(max_length=16)  # 负责账号
    qydz = models.CharField(max_length=64)  # 企业地址
    qyxz = models.CharField(max_length=64)  # 企业性质
    zyyw = models.CharField(max_length=64)  # 主要业务
    djsj = models.CharField(max_length=50, null=True, default="-")  # 登记时间


class JobType(models.Model):
    mc = models.CharField(max_length=16, primary_key=True)  # 账户类别
    sj = models.CharField(max_length=50, null=True, default="-")  # 时间


class Job(models.Model):
    zwlb = models.CharField(max_length=16)  # 职位类别
    zwmc = models.CharField(max_length=50)  # 职位名称
    xz = models.CharField(max_length=16)  # 薪资
    gzdz = models.CharField(max_length=50)  # 工作地址
    nr = models.CharField(max_length=50)  # 内容
    qtxx = models.CharField(max_length=50)  # 其它信息
    fbsj = models.CharField(max_length=50)  # 发布时间
    fbz = models.CharField(max_length=50)  # 发布者
    fbzyhm = models.CharField(max_length=50, default="-1")  # 发布者用户名
    lxdh = models.CharField(max_length=50)  # 联系电话
    jgdm = models.CharField(max_length=50)  # 机构代码
    zt = models.IntegerField(default=1)


class Resume(models.Model):
    tdsj = models.CharField(max_length=50)  # 投递时间
    zt = models.CharField(max_length=20)  # 状态
    hf = models.CharField(max_length=50, null=True)  # 回复
    zwid = models.IntegerField()  # Job ID
    fbz = models.CharField(max_length=16)  # 发布者用户名
    tdz = models.CharField(max_length=16)  # 投递者用户名


class Link(models.Model):
    user0 = models.CharField(max_length=32)
    user1 = models.CharField(max_length=32)


class Message(models.Model):
    user0 = models.CharField(max_length=32)
    user1 = models.CharField(max_length=32)
    time = models.CharField(max_length=32)
    content = models.CharField(max_length=100)
    sender = models.IntegerField()
