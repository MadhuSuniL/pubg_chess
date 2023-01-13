from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from players.models import UserInfo , UserPieacePoses
# Create your views here.

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    username = request.POST['un']
    password = request.POST['ps']
    user = authenticate(username=username,password=password)
    if user is None:
        user = User.objects.create_user(username=username,password=password)
        userinfo = UserInfo.objects.create(username=user.username,status='offline',opponent_username='none',chance=False)
        userpp = UserPieacePoses.objects.create(
            username= user.username,
            kar = '#c91',
            kar2='#c100',
            nade ='#c92',
            nade2='#c99',
            m24 = '#c93',
            m242 ='#c98',
            akm = '#c94',
            akm2 ='#c97',
            awm = '#c95',
            m416 ='#c96',
            shot1='#c81',
            shot2='#c82',
            shot3='#c83',
            shot4='#c84',
            shot5='#c85',
            shot6='#c86',
            shot7='#c87',
            shot8='#c88',
            shot9='#c89',
            shot10='#c90'
            )
    request.session['user'] = user.username
    return redirect('/lobby/'+str(user.username))

def lobby(request,name=None):
    return render(request, "lobby.html")
    