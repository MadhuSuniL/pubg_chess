from django.shortcuts import render
from .extra import get_blinks,reverse_id,make_none
from django.http import JsonResponse
import json
from .models import pieces
from players.models import UserInfo,UserPieacePoses
from django.contrib.auth.models import User
# Create your views here.

def game(req):
    # return render(req, 'login.html')
    return render(req, 'game.html')


def blinks_view(req):
    # print(req.GET)
    id = req.GET['id']
    img = req.GET['img']
    sur = req.GET['surround_cells']
    sur = json.loads(sur)
    res = get_blinks(id, img,sur)
    return JsonResponse(res)


def kill(request):
    id = request.GET['id']
    username = request.session['user']
    # user = User.objects.get(username=username)
    userinfo = UserInfo.objects.get(username=username)
    
    opponent_username = userinfo.opponent_username
    ps = UserPieacePoses.objects.get(username=opponent_username)
    
    if ps.kar == id:
        ps.kar = 'none'
    elif ps.kar2 == id:
        ps.kar2 = 'none'
    elif ps.nade == id:
        ps.nade = 'none'
    elif ps.nade2 == id:
        ps.nade2 = 'none'
    elif ps.m24 == id:
        ps.m24 = 'none'
    elif ps.m242 == id:
        ps.m242 = 'none'
    elif ps.akm == id:
        ps.akm = 'none'
    elif ps.akm2 == id:
        ps.akm2 = 'none'
    elif ps.awm == id:
        ps.awm = 'none'
    elif ps.m416 == id:
        ps.m416 = 'none'
    elif ps.shot1 == id:
        ps.shot1 = 'none'
    elif ps.shot2 == id:
        ps.shot2 = 'none'
    elif ps.shot3 == id:
        ps.shot3 = 'none'
    elif ps.shot4 == id:
        ps.shot4 = 'none'
    elif ps.shot5 == id:
        ps.shot5 = 'none'
    elif ps.shot6 == id:
        ps.shot6 = 'none'
    elif ps.shot7 == id:
        ps.shot7 = 'none'
    elif ps.shot8 == id:
        ps.shot8 = 'none'
    elif ps.shot9 == id:
        ps.shot9 = 'none'
    elif ps.shot10 == id:
        ps.shot10 = 'none'
    ps.save()
    return JsonResponse({"msg":'done...'})
    

def get_backend_pos(request):
    username = request.session['user'] 
    userpp = UserPieacePoses.objects.get(username=username)
    data = {
    "kar" : userpp.kar,
    "kar2": userpp.kar2,
    "nade" : userpp.nade,
    "nade2": userpp.nade2,
    "m24" : userpp.m24,
    "m242" : userpp.m242,
    "akm" : userpp.akm,
    "akm2" : userpp.akm2,
    "awm" : userpp.awm,
    "m416" : userpp.m416,
    "shot1" : userpp.shot1,
    "shot2" : userpp.shot2,
    "shot3" : userpp.shot3,
    "shot4" : userpp.shot4,
    "shot5" : userpp.shot5,
    "shot6" : userpp.shot6,
    "shot7" : userpp.shot7,
    "shot8" : userpp.shot8,
    "shot9" : userpp.shot9,
    "shot10" : userpp.shot10,
    }
    return JsonResponse(data)


def get_opnt_backend_pos(request):
    username = request.session['user'] 
    userinfo = UserInfo.objects.get(username=username)
    opponent_username = userinfo.opponent_username
    
    userpp = UserPieacePoses.objects.get(username=opponent_username)
    data = {
    "kar" : userpp.kar,
    "kar2": userpp.kar2,
    "nade" : userpp.nade,
    "nade2": userpp.nade2,
    "m24" : userpp.m24,
    "m242" : userpp.m242,
    "akm" : userpp.akm,
    "akm2" : userpp.akm2,
    "awm" : userpp.awm,
    "m416" : userpp.m416,
    "shot1" : userpp.shot1,
    "shot2" : userpp.shot2,
    "shot3" : userpp.shot3,
    "shot4" : userpp.shot4,
    "shot5" : userpp.shot5,
    "shot6" : userpp.shot6,
    "shot7" : userpp.shot7,
    "shot8" : userpp.shot8,
    "shot9" : userpp.shot9,
    "shot10" : userpp.shot10,
    }
    
    for key in data:
        data[key] = reverse_id(data[key])
    
    return JsonResponse(data)

def set_backend_pos(request):
    kar = request.GET['kar']
    kar2 = request.GET['kar2']
    nade = request.GET['nade']
    nade2 = request.GET['nade2']
    m24 = request.GET['m24']
    m242 = request.GET['m242']
    akm = request.GET['akm']
    akm2 = request.GET['akm2']
    awm = request.GET['awm']
    m416 = request.GET['m416']
    shot1 = request.GET['shot1']
    shot2 = request.GET['shot2']
    shot3 = request.GET['shot3']
    shot4 = request.GET['shot4']
    shot5 = request.GET['shot5']
    shot6 = request.GET['shot6']
    shot7 = request.GET['shot7']
    shot8 = request.GET['shot8']
    shot9 = request.GET['shot9']
    shot10 = request.GET['shot10']
    username = request.session['user']
    userpp = UserPieacePoses.objects.get(username=username)
    for attr , value in request.GET.items():
        setattr(userpp, attr, value)
    userpp.save()
    
    return JsonResponse({"data":"done"})


def make_none_view(request):
    ids1 = []
    ids2 = []
    username = request.session['user']
    userinfo = UserInfo.objects.get(username=username)
    opponent_username = userinfo.opponent_username
    userpp = UserPieacePoses.objects.get(username=username)
    health = userpp.health
    userpp2 = UserPieacePoses.objects.get(username=opponent_username)
    ids1.append(userpp.kar)
    ids2.append(userpp2.kar)
    ids1.append(userpp.kar2)
    ids2.append(userpp2.kar2)
    ids1.append(userpp.nade)
    ids2.append(userpp2.nade)
    ids1.append(userpp.nade2)
    ids2.append(userpp2.nade2)
    ids1.append(userpp.m24)
    ids2.append(userpp2.m24)
    ids1.append(userpp.m242)
    ids2.append(userpp2.m242)
    ids1.append(userpp.akm)
    ids2.append(userpp2.akm)
    ids1.append(userpp.akm2)
    ids2.append(userpp2.akm2)
    ids1.append(userpp.awm)
    ids2.append(userpp2.awm)
    ids1.append(userpp.m416)
    ids2.append(userpp2.m416)
    ids1.append(userpp.shot1)
    ids2.append(userpp2.shot1)
    ids1.append(userpp.shot2)
    ids2.append(userpp2.shot2)
    ids1.append(userpp.shot3)
    ids2.append(userpp2.shot3)
    ids1.append(userpp.shot4)
    ids2.append(userpp2.shot4)
    ids1.append(userpp.shot5)
    ids2.append(userpp2.shot5)
    ids1.append(userpp.shot6)
    ids2.append(userpp2.shot6)
    ids1.append(userpp.shot7)
    ids2.append(userpp2.shot7)
    ids1.append(userpp.shot8)
    ids2.append(userpp2.shot8)
    ids1.append(userpp.shot9)
    ids2.append(userpp2.shot9)
    ids1.append(userpp.shot10)
    ids2.append(userpp2.shot10)
    
    for id in range(0,len(ids2)):
        ids2[id] = reverse_id(ids2[id])
    
    res = make_none(ids1, ids2)
    return JsonResponse({"data":res,"health":health})


def inc_health(request):
    userpp = UserPieacePoses.objects.get(username=request.session['user'])
    if int(userpp.health) < 100:
        userpp.health = str(int(userpp.health)+5)
        userpp.save()
        if int(userpp.health) > 100:
            userpp.health == '100' 
            userpp.save()
    return JsonResponse({"health":userpp.health+"%"})


def get_health(request):
    userpp = UserPieacePoses.objects.get(username=request.session['user'])
    userinfo = UserInfo.objects.get(username=request.session['user'])
    opponent_username = userinfo.opponent_username
    userpp2 = UserPieacePoses.objects.get(username=opponent_username)
    
    return JsonResponse({"health1":userpp.health+"%","health2":userpp2.health+"%"})


def dec_health(request):
    userinfo = UserInfo.objects.get(username=request.session['user'])
    opponent_username = userinfo.opponent_username
    userpp = UserPieacePoses.objects.get(username=opponent_username)

    if int(userpp.health) > 0:
        num = request.GET['num']
        userpp.health = str(int(userpp.health)-int(num))
        userpp.save()
        if int(userpp.health) < 0:
            userpp.health == '0' 
            userpp.save()
    return JsonResponse({"health":userpp.health+"%"})
