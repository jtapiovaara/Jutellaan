from django.urls import path
from capisco import views

app_name = 'capisco'

urlpatterns = [
    path('', views.kaantaja, name='kaantaja'),
    # path('', views.kielet, name='kielet'),
]