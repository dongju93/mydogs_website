from django.urls import path
from dogs.views import *
from dogs.models import *
from django.views.generic.detail import DetailView


app_name = 'dogs'

urlpatterns = [
    path('info/', info_list, name='info_list'),
    path('infocreate/', infoCreate.as_view(), name='info_create'),
    path('info/update/<int:pk>/', infoUpdate.as_view(), name='info_update'),
    path('info/delete/<int:pk>/', infoDelete.as_view(), name='info_delete'),

    path('daily/', daily_list, name='daily_list'),
    path('dailycreate/', dailyCreate.as_view(), name='daily_create'),
    path('daily/update/<int:pk>/', dailyUpdate.as_view(), name='daily_update'),
    path('daily/delete/<int:pk>/', dailyDelete.as_view(), name='daily_delete'),
    path('daily/detail/<int:pk>/', dailyDetail.as_view(), name='daily_detail'),
    path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list_daily'),

    path('chart/', chartt, name='chart'),

]