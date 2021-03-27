from django.urls import include,path,re_path
from . import views




urlpatterns = [
    path('register/',views.register, name='registration'),
]
