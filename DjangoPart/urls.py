"""TodoList URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from DjangoPart.Views import user, login, user_deal, job_deal, resume_deal

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login.LoginView.as_view()),

    url(r'^register/', user.RegisterView.as_view()),
    url(r'^register_c0/', user.RegisterView_C0.as_view()),
    url(r'^register_c1/', user.RegisterView_C1.as_view()),

    url(r'^get_user_information/', user.GetInformation.as_view()),
    url(r'^update_user_information/', user.UpdateInformation.as_view()),
    url(r'^get_enter_user_information/', user.GetInformation_C.as_view()),
    url(r'^update_enter_user_information/', user.UpdateInformation_C.as_view()),

    url(r'^get_enter_user_validate/', user_deal.UserGet.as_view()),
    url(r'^get_company_user_validate/', user_deal.CompanyGet.as_view()),
    url(r'^get_all_user_normal/', user_deal.NormalGet.as_view()),
    url(r'^get_all_user_freeze/', user_deal.FreezeGet.as_view()),
    url(r'^update_state/', user_deal.StsteUpdate.as_view()),

    url(r'^get_job/', job_deal.JobGet.as_view()),
    url(r'^update_job/', job_deal.JobUpdate.as_view()),

    url(r'^get_job_type/', job_deal.JobTypeGet.as_view()),
    url(r'^update_job_type/', job_deal.JobTypeUpdate.as_view()),

    url(r'^get_resume/', resume_deal.ResumeGet.as_view()),
    url(r'^update_resume/', resume_deal.ResumeUpdate.as_view()),
]
