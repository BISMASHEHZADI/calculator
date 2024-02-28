from django.shortcuts import render,HttpResponse

# Create your views here.


def cal(request):
    re = None
    if request.method=='POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))

        
        if request.POST.get('add') == "add":
            re = num1 + num2
        elif request.POST.get('sub') == "sub":
            re = num1 - num2
        elif request.POST.get('mul') == "multiply":
            re = num1*num2
        elif request.POST.get('div') == "divide":
            if num2==0:
                return HttpResponse('do not use zero')
            else:
               re = num1/num2
        elif request.POST.get('modu') == "modulus":
           re = num1%num2
        else:
            return HttpResponse('please press correct button')
    return render(request,'cal.html',{'result':re})






    # return render(request,'cal.html')

        
