from random import randint, random
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from yaml import dump
from .models import Profile,Post, Puzzle,Question
from json import dumps

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    posts = Post.objects.all()
    return render(request,'index.html', {'user_profile' : user_profile,'posts' : posts})

@login_required(login_url='signin')
def upload(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        title = request.POST['title']
        blog_text = request.POST['main']

        if image and title and blog_text:
            new_post = Post.objects.create(user=user,image=image,title=title,blog_text=blog_text)
            new_post.save()
            
            return redirect('/')
        
        else:
            return redirect('upload')

    else:
        return render(request, 'upload.html', {'user_profile' : user_profile})



@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image'):
            user_profile.profileimg = request.FILES.get('image')
        if request.POST['bio']:
            user_profile.bio = request.POST['bio']
        if request.POST['address']:
            user_profile.address = request.POST['address']
        if request.POST['name']:
            user_profile.name = request.POST['name']
        user_profile.save()

        return redirect('settings')

    return render(request,'settings.html',{'user_profile' : user_profile})


def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password2']
        password2 = request.POST['password1']

        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password = password1)
                user.save()

                # log user in and redirect to settings page

                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)

                # create a profile object for the new user

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')

    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('signin')


def puzzle(request):
    
    puzzles = Puzzle.objects.all()

    lnth = len(puzzles)

    x = randint(0,lnth-1)

    data = [puzzles[x].title, puzzles[x].question, puzzles[x].ans]

    data = dumps(data)

    return render(request, 'puzzle.html', {'data' : data})

def quiz(request):
    
    questions = Question.objects.all()

    lnth = len(questions)

    vis = [False]*lnth

    data = []

    while len(data) < 5:
        x = randint(0,lnth-1)
        if vis[x] == False:
            vis[x] = True

            miniData = [questions[x].question, questions[x].option1, questions[x].option2, questions[x].option3, questions[x].option4, questions[x].ans]
            data.append(miniData)
    
    data = dumps(data)

    return render(request, 'quiz.html', {'data' : data})