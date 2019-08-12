import  os
import json
if os.path.exists('weather.json'):    # 在本地文件取json
    f = open('weather.json', encoding='utf-8')
    city_list = json.loads(f.read())
    for x in range(len(city_list)):
        a = len(city_list)
        # 取到值，然后 根据键名找数据
        city_code = city_list[x]["city_code"]
        city_name = city_list[x]['city_name']
        # 创建个字典，往字典里添加数据
        dict_city = {
            city_name:int(city_code),
        }
        print(dict_city)
        # 创建文件，写入数据
        c = open('list_city','a',encoding='utf-8')
        #
        c.write(str(dict_city).replace('{','').replace('}','')+',')
        c.close()



