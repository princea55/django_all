from django.urls import path
from django_model.views import django_model_choice, django_model_primary_key, django_model_many_to_many, \
    order_with_respect_to

urlpatterns = [
    # category CURD operations
    path('choice/', django_model_choice, name='choice'),
    path('primary-key/', django_model_primary_key, name='primary-key'),
    path('many-to-many/', django_model_many_to_many, name='many-to-many'),
    path('order_with_respect_to/', order_with_respect_to, name='order_with_respect_to'),



]
