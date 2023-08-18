from django.shortcuts import render

# Create your views here.

def data_render(request):
    d={'name':'kajal','age':15}
    return render(request,'data_render.html',context=d)

def condition(request):
    d={'a':30,'b':100,'c':80,'hobbies':['cricket','football']}
    return render(request,'condition.html',context=d)

