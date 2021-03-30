
from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,CommentForm,ProfileForm,UserUpdateForm,RegistrationForm
from .models import Image, Profile,Comment,Followwww
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView
)

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comments = Comment.objects.all()
    # profile = Profile.objects.filter(user=Image.profile.id).first()
    # print('posts',posts)
    return render(request,'index.html',{"posts":posts,"profile":profile,"comments":comments})

@login_required(login_url='/accounts/login/')
def newPost(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)        
        if form.is_valid():
            image=form.cleaned_data.get('image')
            imageCaption=form.cleaned_data.get('imageCaption')
            post = Image(image = image,imageCaption= imageCaption, profile=user_profile)
            post.savePost()
            
        else:
            print(form.errors)

        return redirect('home')

    else:
        form = NewPostForm()
    return render(request, 'newPost.html', {"form": form})
    
@login_required(login_url='/accounts/login/')    
def profile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = profileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('home')

    else:
        
        profile_form = ProfileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', params)

def prof(request):
    # user_prof = get_object_or_404(User, username=username)
    # if request.user == user_prof:
    #     return redirect('profile', username=request.user.username)
    profile = Profile.objects.filter(user = request.user)
    return render(request,"users/profile.html",{"profile":profile})


def editProfile(request):
    if request.method == 'POST':

        userForm = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=request.user)

        if  profile_form.is_valid():
            userForm.save()
            profile_form.save()

            return redirect('profile')

    else:
        
        profile_form = ProfileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'editprofile.html', params)

@login_required(login_url='/accounts/login/')
def comment(request,id):
    comments = Comment.objects.filter(postt= id)
    images = Image.objects.filter(id=id).all()
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    image = get_object_or_404(Image, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.postt = image
            comment.userr = user_profile
            comment.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = CommentForm()
    return render(request,'comment.html',{"form":form,"images":images,"comments":comments})

def searchprofile(request): 
    if 'searchUser' in request.GET and request.GET['searchUser']:
        name = request.GET.get("searchUser")
        searchResults = Profile.search_profile(name)
        message = f'name'
        params = {
            'results': searchResults,
            'message': message
        }
        return render(request, 'results.html', params)
    else:
        message = "You haven't searched for any image category"
    return render(request, 'results.html', {'message': message})

class PostDetailView(DetailView):
    model = Image
    template_name= 'index.html'
    def get_context_data(self, *args, **kwargs):
        context=super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff=get_object_or_404(Image, id=self.kwargs['id'])
        total_likes=stuff.total_likes()
        context["total_likes"]=total_likes
        return context    

def likePost(request,id):
    post= get_object_or_404(Image, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    # return HttpResponseRedirect(reverse('home', args=[str(id)]))
    return HttpResponseRedirect(request.path_info)

class UserListView(ListView):
    model=Profile
    template_name='posts/view.html'
    context_object_name='posts'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)
            # user = get_object_or_404(User, username=self.kwargs.get('username'))
            # return Image.objects.filter(author=user.profile).order_by('-date_posted')

class ProfileDetailView(DetailView):
    model=Profile
    template_name='posts/detail.html'
    context_object_name='posts'

    def get_object(self, **kwargs):
        id=self.kwargs.get('pk')
        prof=Profile.objects.get(pk=id)
        return prof

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        avi=self.get_object()
        myProf=Profile.objects.get(user=self.request.user)
        if avi.user in myProf.following.all():
            follow=True
        else:
            follow=False
        context["follow"]=follow
        return context



def follow_unfollow(request):

    if request.method=='POST':
        my_profile=Profile.objects.get(user=request.user)
        pk= request.POST.get('follow')
        obj=Profile.objects.get(id=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return HttpResponseRedirect(request.path_info)
        # return redirect('profile-list-view ')
def folo(request,id):
    current_user = request.user
    usertoFollow = User.objects.get(id = id)
    follow = Followwww(user,usetoFollow)
    follow.save()
    return HttpResponseRedirect(request.path_info)


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=ProfileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()

            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=ProfileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)    