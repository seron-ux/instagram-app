from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm
from .models import Image

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    posts = Image.objects.all()
    return render(request,'index.html',{"posts":posts,"profile":profile,"comments":comments})

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
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
        # prof=profileForm()
    params={
        'form':form,
        # 'profForm': prof
    }
    return render(request, 'users/register.html', params) 

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
    



