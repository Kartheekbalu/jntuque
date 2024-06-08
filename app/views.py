from django.shortcuts import render,redirect,get_object_or_404
from app.models import upload
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages,auth
from datetime import datetime
from django.core.paginator import Paginator


# Create your views here.
def Home(request):
    uploads = upload.objects.all()
    paginator = Paginator(uploads,4)  # Show 2 uploads per page.
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    context = {
        'data': data
    }
    return render(request, 'home.html', context)


def Register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')
                
        user=User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        messages.success(request,'Signed up successfully!....')
        return redirect('signin')

    return render(request,'register.html')


def Signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('user',id=user.id)
        else:
            messages.error(request, 'Invalid username or password')
            return render(request,'signin.html')
    return render(request, 'signin.html')


def Signout(request):
    logout(request)
    return redirect('/')

def user(request,id):
    user_id = request.user.id
    user = request.user
    name = user.username
    papers = upload.objects.filter(username=name)
    
    paginator = Paginator(papers,4)  # Show 2 uploads per page.
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    upload_count = papers.count()
    context = {
        'user': name,
        'papers': data,
        'user_id': user_id,
        'upload_count': upload_count
    }
    return render(request,'user.html',context)

def Upload(request,id):
    #user_id = request.user.id
    user=User.objects.get(id=id)
    name=user.username
    if request.method=='POST':
        img=request.FILES.get('img')
        sub=request.POST.get('subject')
        branch=request.POST.get('branch')
        reg=request.POST.get('regulation')
        year=request.POST.get('year')
        date=datetime.now()
        
        if img is None:
            messages.error(request, 'No file uploaded.')
            return render(request, 'upload.html')
        
        new=upload.objects.create(username=name,pic=img,subject=sub,branch=branch,regulation=reg,year=year,date=date)
        new.save()
        messages.success(request,'Uploaded successfully!....')
        return redirect('user',id=user.id)
    return render(request,'upload.html',{'user_id': id})

def search(request):
    query=request.GET['q']
    data=upload.objects.filter(subject__icontains=query)
    return render(request,'search.html',{'post':data})

def filters(request):
    reg=request.GET['regulation']
    year=request.GET['year']
    branch=request.GET['branch']
    data=upload.objects.filter(regulation__icontains=reg, year__icontains=year, branch__icontains=branch)
    return render(request,'filters.html',{'data':data})
    

def Pic(request, upload_id):
    papers = upload.objects.filter(id=upload_id)
    context = {
        'papers': papers
    }
    return render(request, 'pic.html', context)


def update(request, id):
    post = get_object_or_404(upload, id=id)
    
    if request.method == "POST":
        img = request.FILES.get('pic')
        subject = request.POST.get('subject')
        branch = request.POST.get('branch')
        regulation = request.POST.get('regulation')
        year = request.POST.get('year')

        if img:
            post.pic = img
        post.subject = subject
        post.branch = branch
        post.regulation = regulation
        post.year = year
        post.save()
        return redirect('user',id=id)
    return render(request, 'update.html', {'post': post})

def dlt(request,id):
    rem=upload.objects.get(id=id)
    rem.delete()
    return redirect('user',id=id)