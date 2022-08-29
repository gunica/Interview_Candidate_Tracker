from django.conf.urls import url
from CandidateApp import views

urlpatterns=[
    url(r'^candidate$',views.listApi),
    url(r'^candidate/([0-9]+)$',views.listApi)
]