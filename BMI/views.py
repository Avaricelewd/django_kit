from django.shortcuts import render

# Create your views here.



def BMI(request):
    if request.method == 'GET':
        return render(request, 'BMI/BMI.html')
    elif request.method == 'POST':
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        if height == '' or weight == '':
            return render(request, 'BMI/BMI.html')
        else:
            set = int(height)*0.01
            BMI = int(weight)/(set*set)

            if BMI <= 18.4:
                a = '偏瘦'
            elif 18.5< BMI<=23.9:
                a = '正常'
            elif 24.0 < BMI <=27.9:
                a = '过重'
            elif BMI>= 28.0:
                a = '肥胖'
            # print(BMI)
            context = {
                    'BMI':BMI,
                    'a':a,
                }
            return render(request,'BMI/BMI.html',context)