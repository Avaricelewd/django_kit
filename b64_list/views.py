from django.shortcuts import render
import base64
# Create your views here.


def b64(request):
    if request.method =='GET':
        return render(request, 'b64_list/b64.html')
    elif request.method == 'POST':
        text= request.POST.get('text')
        content_list =text.encode(encoding='utf-8')
        b64_content = base64.b64encode(content_list)
        b64_content_str = b64_content.decode()
        context = {
            'b64_content_str':b64_content_str,
        }
        return render(request,'b64_list/b64.html',context=context)


def b64_j(request):
        if request.method == 'GET':
            return render(request, 'b64_list/b64.html')
        elif request.method == 'POST':
            content_str = request.POST.get('cont')
            c = base64.b64decode(content_str)
            context = {

                'c':c.decode(),
            }
            return render(request,'b64_list/b64.html',context=context)