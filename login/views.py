from django.shortcuts import render
from django.shortcuts import HttpResponse
from login import models

# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username, password)
#     return render(request, 'index.html')
user_list = []


def index(request):
    # return  HttpResponse("HELLO WORD")
    # return  render(request,"index.html")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user': username, 'pwd': password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)
    # 读取所有
    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'data': user_list})
