from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^process/reg/', views.register, name='reg'),
    url(r'^process/log/', views.login, name='log'),
    url(r'^success/', views.success, name='success'),
]
