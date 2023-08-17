from django.urls import path
from .import views
# app_name='home'

urlpatterns=[

    # path('index',views.index,name='index'),
    path('homepage',views.homepage,name='homepage'),
]