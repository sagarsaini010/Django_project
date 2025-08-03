from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *

def welcome(request):
    template = loader.get_template('welcome.html')
    return HttpResponse(template.render())

def candidateRegistrationForm(request):
    res = render(request,'registration_form.html')
    return res

def candidateRegistration(request):
    if request.method == 'POST':
        username = request.POST['username']
        if (len(Candidate.objects.filter(username=username))):
            userStatus = 1
        else:
            candidate = Candidate()
            candidate.username=username
            candidate.password=request.POST['password']
            candidate.name=request.POST['name']
            candidate.save()
            userStatus =2
    else:
        userStatus= 3 #Request method is not POST
    context = {
        'userStatus' : userStatus
    }
    res = render(request,'registration.html',context)
    return res

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        candidate=Candidate.objects.filter(username=username,password=password)
        if len(candidate)==0:
            loginError='Invalid Username or Password'
            res = render(request,'login.html',{'loginError':loginError})
        else:
            #login Success
            request.session['username'] =candidate[0].username
            request.session['name']= candidate[0].name
            res=HttpResponseRedirect("home")
    else:
        res = render(request,'login.html')
    return res
    

def candidateHome(request):
    if 'name' not in request.session.keys():
        res = HttpResponseRedirect('login')
    else:
        res = render(request,'home.html')
    return res


def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass
