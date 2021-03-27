from django.urls import include,path,re_path
from . import views




urlpatterns = [
    path('',views.index,name = 'home'),
    path('register/',views.register, name='registration'),
]
