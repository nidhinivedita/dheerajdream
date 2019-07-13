from django.shortcuts import render

# Create your views here.
def Wish(request):
    return render(request,'testapp/login.html')
def Hello(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'testapp/hello.html',{'count':newcount})
    response.set_cookie('count',newcount,max_age=1800)
    return response
