
from django.urls import include,path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.index,name = 'home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('register/',views.register, name='registration'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('accounts/register/', auth_views.LoginView.as_view(template_name='users/register.html'), name='register'),
    path('new/post/', views.newPost, name='newPost'),
    path('comment/<id>', views.comment, name='comment'),
    path('profile/', views.profile, name='profile'),
    path('prof/', views.prof, name='prof'),
    path('edit_profile/', views.editProfile,name = 'update_profile'),
    path('search/', views.searchprofile, name='search'),
    path('follow/', views.follow_unfollow, name='follow'),
    path('like/<id>/', views.likePost, name='like_post'),
    path('profiles/', views.UserListView.as_view(), name='profile-list-view'),
    path('profiles/<pk>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)