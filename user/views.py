from django.shortcuts import render
from user.models import Users
from hashlib import sha256
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_obj = Users.objects.filter(username=username)
    if len(user_obj)==1:
        return JsonResponse({'status':'403'})
    elif len(user_obj)==0:
        user = Users(username=username,password=sha256(password.encode('utf-8')).hexdigest())
        user.save()
        return JsonResponse({'status':'200'})
    else:
        return JsonResponse({'status':'500'})
    
@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user_obj = Users.objects.filter(username=username,password=sha256(password.encode('utf-8')).hexdigest())
    if len(user_obj)==1:
        return JsonResponse({'status':'200'})
    elif len(user_obj)==0:
        return JsonResponse({'status':'404'})
    else:
        return JsonResponse({'status':'500'})

    