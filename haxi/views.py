from django.shortcuts import render

import hashlib
# Create your views here.


def haxi_list(request):
    if request.method == 'GET':
        return render(request,'haxi/haxi.html')
    elif request.method == 'POST':
        text = request.POST.get('t')
        # print(text)
        sha256 = hashlib.sha256()
        sha256.update(text.encode('utf-8'))
        a = sha256.hexdigest()
        # print(a)
        context = {
            'text':text,
            'a':a,
        }
        return render(request,'haxi/haxi.html',context=context)