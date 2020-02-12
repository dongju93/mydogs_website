from django.urls import path
from coupon.views import add_coupon

app_name = 'coupon'

urlpatterns = [
    path('add/', add_coupon, name='add'),
]