from django.shortcuts import render

from student_vote import models
from .models import option
import threading

# Create your views here.
# 定义ip_list
ip_list = []
# 投票首页，获取投票人名字，跳转到投票页面
def index(request):
    if request.method == 'GET':
        return render(request, 'student_vote/index.html', context={})
    elif request.method == 'POST':
        name = request.POST["name"]
        if name == '':
            return render(request, 'student_vote/index.html', context={})
        else:
            # 用id查询用户名字
            id = option.objects.get(name=name)
            idd = id.id
            context = {
                "idd": idd,
                "name": name,
            }
            return render(request, 'student_vote/index2.html', context)

# 输入用户名字，进行投票
def select(request):
    if request.method == 'GET':
        return render(request, 'student_vote/index.html', context={})
    elif request.method == 'POST':
        ip = request.META['REMOTE_ADDR']
        # print(ip)
        print(ip_list)
        if ip in ip_list:
            return render(request, 'student_vote/index.html')
        else:
            # 拿到用户ip，存到ip_list
            ip_list.append(ip)
            # name = request.POST.get('name')
            name = request.POST["name"]
            # print(name)
            # 前端用的渲染，在这也得用转义，获取前端传来的参数
            value = request.POST.get(f"{name}")
            con = option.objects.get(name=name)
            name = con.name
            # 从前端拿到数据以后，把拿到的数据存到数据库
            if name is None:
                return render(request, 'student_vote/index.html')
            elif value == '0':
                stu = option.objects.get(name=name)
                stu.waiver = stu.waiver + 1
                stu.save()
            elif value == '1':
                stu = option.objects.get(name=name)
                stu.support = stu.support + 1
                stu.save()
            elif value == '2':
                stu = option.objects.get(name=name)
                stu.onsupport = stu.onsupport + 1
                stu.save()
            # 从数据库提取支持的票数，用来计算支持率
            con = option.objects.get(name=name)
            support = con.support
            # 用ip数 实现百分比算法
            Percentage = int(round(support / len(ip_list), 2) * 100)
            # print(Percentage)
            message = '为了确保数据准确，不可重复提交！'
            context = {
                'name': name,
                'Percentage': Percentage,
                'message':message,
            }
            return render(request, 'student_vote/index2.html', context)

# 添加操作，如果数据库没有投票的人时，可以进行手动添加
def add(request):
    if request.method == 'GET':
        return render(request, 'student_vote/add.html', context={})
    elif request.method == 'POST':
        name = request.POST['name']
        name_list = []
        for names in option.objects.all():
            name_list.append(names.name)
        if name in name_list:
            message = '名字已有，请勿重复添加'
            return render(request,'student_vote/add.html',context={
                'message':message
            })
        else:
            models.option.objects.create(name=name)
            message = '添加成功，请返回'
            return render(request,'student_vote/add.html',context={
                'message':message
            })

def result(request):
    if request.method == 'GET':
        return render(request, 'student_vote/result.html')
    elif request.method == 'POST':
        name = request.POST["name"]
        if name == '':
            return  render(request,'student_vote/result.html')
        else:
            name_list = option.objects.get(name=name)
            a = name_list.name
            support = name_list.support
            waiver = name_list.waiver
            onsupport = name_list.onsupport
            total = support +onsupport+waiver
            print(a,support,onsupport,waiver ,total)
            Percentage = int(round(support / len(ip_list), 2) * 100)
            content = {
                'name':name,
                'total':total,
                'support':support,
                'onsupport':onsupport,
                'waiver':waiver,
                'Percentage':Percentage
            }

            return render(request,'student_vote/result.html',context=content)


# 重启服务器时，刷新数据库操作
def refresh():
    for name in option.objects.all():
        name.support =0
        name.onsupport = 0
        name.waiver = 0
        name.save()

refresh()

# def student_vote():
#     return
#
# for i in range(31):
#     t = threading.Thread(target=student_vote)
#     t.start()