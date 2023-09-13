from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import Posts,Comments
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required,permission_required
from .forms import PostForm,CommentForm

# Create your views here.

def home(request):
    all_posts = Posts.objects.all().order_by("-created_at")
    paginator = Paginator(all_posts,2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',{'posts':page_obj})

def postlist(request):
    all_posts = Posts.objects.all().order_by("-created_at")
    return render(request,'postlist.html',{'posts':all_posts})

def error(request):
    return render(request,'error.html')

def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request,'login.html')

def signupview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            password = password1
            user = User.objects.create_user(username=username,email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            
    return render(request,'signup.html')

def logoutview(request):
    logout(request)
    return redirect('/login')

@permission_required('posts.add_posts',login_url='error')
def postcreate(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'postcreate.html',{'form':form})


@permission_required('posts.change_posts',login_url='error')
def postupdate(request,post_id):
    post = Posts.objects.get(id=post_id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post.title = title
        post.content = content
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')
        post.save()
        return redirect('/posts/')
    return render(request,'postupdate.html',{'post':post})

@permission_required('posts.delete_posts',login_url='error')
def postdelete(request,post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    return redirect('/posts/')

def postdetail(request,post_id):
    post = Posts.objects.get(id=post_id)
    comments = Comments.objects.filter(post_id=post_id)
    form = CommentForm()
    return render(request,'postdetail.html',{'post':post,'form':form,'comments':comments})

@login_required(login_url='login')
def commentcreate(request,post_id):
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('content')
            cmt = Comments.objects.create(
                author_id = request.user.id,
                post_id = post_id,
                content = data
            )
            cmt.save()
        return redirect(f'/posts/{post_id}')
    
@login_required(login_url='login')
def commentupdate(request,post_id,cmt_id):
    cmt = Comments.objects.get(id=cmt_id)
    if request.method == "POST":
        cmt.author_id = request.user.id
        cmt.post_id = post_id
        cmt.content = request.POST.get('cmt')
        cmt.save()
        return redirect(f'/posts/{post_id}')

@login_required(login_url='login')   
def commentdelete(request,post_id,cmt_id):
    cmt = Comments.objects.get(id=cmt_id)
    cmt.delete()
    return redirect(f'/posts/{post_id}')