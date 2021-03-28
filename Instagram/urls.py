from django.urls import include,path,re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.index,name = 'home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/',views.register, name='registration'),
    path('new/post/', views.newPost, name='newPost'),
     path('comment/<id>', views.comment, name='comment'),
]
