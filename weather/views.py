from django.shortcuts import render
import requests
import json
from static.weather import json_list
# Create your views here.

def index2(request):

    return render(request,'index/index.html',context={})
def index(request):
        city_code =   101100701      #   101180101
        url = f'http://t.weather.sojson.com/api/weather/city/{city_code}'
        # resp = urllib.request.urlopen(url=url).read().decode()
        resp = requests.get(url=url)
        # print(resp.text)
        data = json.loads(resp.text)['data']
        # 地区
        cityInfo = json.loads(resp.text)['cityInfo']
        parent = cityInfo['parent']
        city = cityInfo['city']
        # 时间
        time = json.loads(resp.text)['time']
        # print(parent,city,time)
        #具体信息

        forecast = data['forecast']
        high = forecast[0]['high']
        low = forecast[0]['low']
        week = forecast[0]['week']
        ymd = forecast[0]['ymd']
        type = forecast[0]['type']
        shidu = data['shidu']
        pm25 = data['pm25']
        quality = data['quality']
        ganmao = data['ganmao']
        context = {
            'time':time,
            'parent':parent,
            'city':city,
            'forecast':forecast,
            'data':data,
            'shidu':shidu,
            'pm25':pm25,
            'quality':quality,
            'ganmao':ganmao,
            'high':high,
            'low':low,
            'week':week,
            'ymd':ymd,
            'type':type
             }
        return render(request,'weather/index.html',context)


def select(request):
    if request.method == 'GET':
        return  render(request,'weather/select.html')
    elif request.method == 'POST':
        address = request.POST.get('address')

        city = json_list.json_city[f'{address}']
        id = f"{city}"
        print(id,city)
        url = requests.get(f'http://t.weather.sojson.com/api/weather/city/{id}')
        status_code = url.status_code
        if status_code == 200:
            resp = url.text
        # resp = requests.get(url=url)
        # print(resp.text)
            data = json.loads(resp)['data']
            # 地区
            cityInfo = json.loads(resp)['cityInfo']
            parent = cityInfo['parent']
            city = cityInfo['city']
            # 时间
            time = json.loads(resp)['time']
            # print(parent,city,time)
            # 具体信息

            forecast = data['forecast']
            high = forecast[0]['high']
            low = forecast[0]['low']
            week = forecast[0]['week']
            ymd = forecast[0]['ymd']
            type = forecast[0]['type']
            shidu = data['shidu']
            pm25 = data['pm25']
            quality = data['quality']
            ganmao = data['ganmao']
            context = {
                'time': time,
                'parent': parent,
                'city': city,
                'forecast': forecast,
                'data': data,
                'shidu': shidu,
                'pm25': pm25,
                'quality': quality,
                'ganmao': ganmao,
                'high': high,
                'low': low,
                'week': week,
                'ymd': ymd,
                'type':type,
            }

            return render(request,'weather/select.html',context)


