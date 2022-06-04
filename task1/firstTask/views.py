from django.http import HttpResponseRedirect
from django.shortcuts import  render
from .main import *

    
def index(request):
    value = {}
    if request.method == 'POST':
        value['result'] = float(request.POST.get('input')) 
        value['temp'] = value['result'] 
        percentage = percent(value['result'])
        value['result'] = percentage
    return render(request, 'home.html',value)