from django.shortcuts import render
import requests,re,json
from bs4 import BeautifulSoup
from urllib import request
from lxml import etree
# Create your views here.


def video(request):
    if request.method == 'GET':
        return render(request, 'video_jx/video.html')
    elif request.method == 'POST':
        url1 = request.POST.get('video')
        sever = 'http://api.xfsub.com'
        # api = 'http://api.xfsub.com/xfsub_api/?url='
        api = 'http://api.xyingyu.com/?url='
        get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
        url = url1.split('#')[0]
        target = api + url
        print(target)
        s = requests.session()
        req = s.get(url=target)
        print(req)
        req.encoding='utf-8'
        # info = json.loads(re.findall('"url.php",\ (.+),', req.text))
        root = etree.HTML(req.text)
        src = root.xpath("//iframe[@id='player']/@src")[0]
        a = requests.get(src)
        b = etree.HTML(a.content)
        print(src)
        # print(a.content.decode('utf-8'))
        # print(src)
        #         # context={
        #         #     'src':src
        #         # }
        #         # c = open('C:\\Users\亓、彧\PycharmProjects\django_kit\static\\video_src\src.txt','w')
        #         # c.write(src)
        #         # c.close()
        return render(request,'video_jx/video.html',context={})