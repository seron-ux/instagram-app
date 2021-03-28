from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,CommentForm,ProfileForm
from .models import Image,Comment

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
        
        profile_form = profileForm(instance=request.user)
        user_form = UserUpdateForm(instance=request.user)

        params = {
            'user_form':user_form,
            'profile_form': profile_form

        }

    return render(request, 'profile.html', params)
    



