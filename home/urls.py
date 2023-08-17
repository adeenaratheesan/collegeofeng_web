from django.urls import path,include
from .import views
app_name='home'

urlpatterns=[

    # path('index/',views.index,name='index'),
    path('homepage/',views.homepage,name='homepage'),
    path('login/',views.login,name='login'),
    path('onlineadmission/',views.onlineadmission,name='onlineadmission'),
    path('sample/',views.sample,name='sample'),

]