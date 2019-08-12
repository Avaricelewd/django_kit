from django.shortcuts import render
import json
# Create your views here.

def list_json(request):
    if request.method == 'GET':
        return render(request,'list_json/list_json.html')
    elif request.method == 'POST':

        json_str = request.POST.get('json')
        if json_str ==  '':
            return render(request, 'list_json/list_json.html')
        else:
            json_str = request.POST.get('json')
            json_list = json.loads(json_str)
            context = {
                'json_list':json_list,
            }
            return render(request,'list_json/list_json.html',context=context)

def json_raw(request):
    if request.method == 'GET':
        return render(request, 'list_json/list_json.html')
    elif request.method == 'POST':

        json_raw = request.POST.get('json_jx')
        if json_raw == '':
            return render(request, 'list_json/list_json.html')
        else:
            json_raw = request.POST.get('json_jx')
            json_list_raw = json.dumps(json_raw)
            a = json_list_raw.encode(encoding='utf-8')
            # print(json_list_raw)
            context = {
                'json_list_raw': json_list_raw,
            }
            return render(request, 'list_json/list_json.html', context=context)