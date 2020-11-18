from django.urls import path
from capisco import views

app_name = 'capisco'

urlpatterns = [
    path('', views.kaantaja, name='kaantaja'),
    path('vaihdafkieli', views.vaihdafkieli, name='vaihdafkieli'),
    path('vaihdatkieli', views.vaihdatkieli, name='vaihdatkieli')
    # path('', views.kielet, name='kielet'),
]