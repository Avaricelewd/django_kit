from django.shortcuts import render

import os
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request, 'chat/login.html', context={})
    elif request.method == 'POST':
        his_name = request.POST.get('his_name')
        your_name = request.POST.get('your_name')
        if his_name == '':
            return render(request,'chat/login.html')
        elif your_name == '':
            return render(request,'chat/login.html')
        his_avatar = request.FILES.get('your_avatar')
        your_avatar = request.FILES.get('his_avatar')
        print(type(his_avatar),type(your_avatar))
        # ads = './static/image/'
        ads= 'C:\\Users\亓、彧\PycharmProjects\django_kit\static\image'
        os.chdir(ads)
        if os.path.exists(your_avatar.name) or os.path.exists(his_avatar.name):
            path1 = 'his_avatar'
            path2 = 'your_avatar'
            file1 = os.path.splitext(path1)
            file2 = os.path.splitext(path2)
            filename1,type1 = file1
            filename2,type2 = file2
            print(filename1)
            print(filename2)
            print(type1)
            print(type2)
        else:
            with open(your_avatar.name,'wb+') as f:
                f.write(your_avatar.read())
                f.close()
            with open(his_avatar.name,'wb+') as f:
                f.write(his_avatar.read())
                f.close()
            print(your_avatar.name)
            print(555555555555,his_avatar,your_avatar)
        global context
        context = {
            'your_name':your_name,
            'his_name':his_name,
            'his_avatar':his_avatar,
            'your_avatar':your_avatar,
        }
        return render(request,'chat/login.html',context)


def index(request):
    return render(request,'chat/index.html',context)

def index2(request):
    return render(request,'chat/index2.html',context={})