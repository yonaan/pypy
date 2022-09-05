from multiprocessing import current_process
from re import S
import string
from time import strftime
from datetime import datetime
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render,HttpResponseRedirect,reverse
from numpy import true_divide
from .models import MasterSensor, MasterThreshold, Temperature_Data, Temperature_Trend

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
#from django.shortcuts import HttpResponseRedirect
  
def monitor(request):
    try:
        t=Temperature_Data.objects.all()
    except:
        t= None
    return (render(request,'mon/monitor.html', context={'ac':t}))


def monitor_graph(request):
    try:
        qs=Temperature_Trend.objects.all()

    except:
        qs= None
    context={'qs':qs}      
    return render(request,'mon/monitor_graph.html', context)

def sensors(request):
    try:
        sensor=MasterSensor.objects.all()
    except:
        sensor= None
    return (render(request,'mon/sensors.html', context={'ac':sensor}))

    #return (render(request,'mon/index.html', context={'ac':Event}))

def threshold_view(request):
    try:
        threshold=MasterThreshold.objects.all()
        qsi = MasterSensor.objects.all()

    except:
        threshold= None
    return (render(request,'mon/threshold_view.html', context={'ac':threshold,'qsi':qsi}))


def signup(request):        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form': form})
   
def landing(request): 
    return render(request, 'accounts/landing.html')
   
def home(request): 
    return render(request, 'mon/home.html')
  
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/landing.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'accounts/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
  
   
def signout(request):
    logout(request)
    return redirect('/')


def add(request):
    if(request.method == "POST"):
        a = MasterSensor()
        error_free = True
        # if(request.POST["sensor_id"]):
        a.sensor_id = datetime.now().strftime("%y%m%d%H%M%S")
        # else:
        #     error_free = False
        if(request.POST["sensor_description"]):
            a.sensor_description = request.POST["sensor_description"]
        else:
            error_free = False
        if(request.POST["created_by"]):
            a.created_by = request.POST["created_by"]
        else:
            error_free = False
        if(request.POST["updated_by"]):
            a.updated_by = request.POST["updated_by"]
        else:
            error_free = False
        if(not error_free):
            return(render(request, 'error.html'))
        a.save()
        return(HttpResponseRedirect(reverse('sensors')))
    return (render(request, 'mon/add.html'))

def Threshold_add(request):
    qs = MasterSensor.objects.all()

    if(request.method == "POST"):
        a = MasterThreshold()
        error_free = True
        a.threshold_id = datetime.now().strftime("%y%m%d%H%M%S")
        if(request.POST["sensor_id"]):
            for q in qs:
                if q.sensor_id == request.POST["sensor_id"]:
                    a.sensor_id = q
        else:
            error_free = False
        if(request.POST["threshold_description"]):
            a.threshold_description = request.POST["threshold_description"]
        else:
            error_free = False
        if(request.POST["sensor_warning"]):
            a.sensor_warning = request.POST["sensor_warning"]
        else:
            error_free = False
        if(request.POST["sensor_danger"]):
            a.sensor_danger = request.POST["sensor_danger"]
        else:
            error_free = False
        if(not error_free):
            return(render(request, 'error.html'))
        a.save()
        return(HttpResponseRedirect(reverse('threshold_view')))

    context={'qs':qs}
    return render(request, 'mon/threshold_add.html', context)

def device_add(request):
    qsii = MasterThreshold.objects.all()
    qsi = MasterSensor.objects.all()
    if(request.method == "POST"):
        a = Temperature_Data()
        error_free = True
        a.device_id=datetime.now().strftime("%y%m%d%H%M%S")
        if(request.POST["sensor_id"]):
            for y in qsi:
                if y.sensor_id == request.POST["sensor_id"]:
                    a.sensor_id = y
        else:
            error_free = False

        if(request.POST["threshold_id"]):
            for q in qsii:
                if q.threshold_id == request.POST["threshold_id"]:
                    a.threshold_id = q
        else:
            error_free = False
            
        if(request.POST["device_name"]):
            a.device_name = request.POST["device_name"]
        else:
            error_free = False
        if(request.POST["created_by"]):
            a.created_by = request.POST["created_by"]
        else:
            error_free = False
        if(not error_free):
            return(render(request, 'error.html'))
        a.save()
        return(HttpResponseRedirect(reverse('monitor')))

    context={'qsii':qsii, 'qsi':qsi}
    return render(request, 'mon/device_add.html', context)


def tempedit(request, edit_id):
    if(request.method == "POST"):
        a = MasterThreshold.objects.get(id=edit_id)
        error_free = True
        change = False
        if(request.POST["sensor_warning"]):
            a.sensor_warning = request.POST["sensor_warning"]
            change = True
        else:
            error_free = False
        if(request.POST["sensor_danger"]):
            a.sensor_danger = request.POST["sensor_danger"]
            change = True
        else:
            error_free = False

        if(not error_free):
            return(render(request, 'mon/error.html', context={'err': "Please fill", "back": edit_id}))
        if(not change):
            return(render(request, 'mon/error.html', context={'err': "NOTHING changed", "back": edit_id}))

        a.save()
        return(HttpResponseRedirect(reverse('threshold_view')))
    return (render(request, 'mon/tempedit.html', context={'edit_id': edit_id}))

def delete(request, id):
    try:
        MasterSensor.objects.get(id=id).delete()
    except:
        return(render(request, 'mon/error.html', context={'err': "WRONG ID", "back": "/"}))
    
    return(HttpResponseRedirect(reverse('home')))

#def stat():
    if():
        a = event.objects.get()
        if a.current_temp < a.min_temp :
            a.status='good'
        if a.current_temp >= a.min_temp and a.current_temp < a.max_temp:
            a.status='warning'
        else: a.status='danger'
        
        a.save()
        return(HttpResponseRedirect(reverse('index')))
#def save_temp_data(self):
  #  temp_data=
#e=event()
#if(e.current_temp<e.min_temp):
  #  e.status = ['good']
   # if(e.min_temp<=e.current_temp<e.max_temp):
    #    e.status = ['warning']
    #else: 
    # e.status=['danger']