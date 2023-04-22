from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.
def index1(request):

    dests=Destination.objects.all()
    '''
    dest1 = Destination()
    dest1.name = 'Rajahmundry'
    dest1.price = 700
    dest1.desc = 'distric of AP'
    dest1.caps=' Godhavri River '
    dest1.img = " destination_1.jpg "
    dest1.offer = False

    
    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.price = 1000  
    dest2.desc = 'capital of TS'
    dest2.caps=' Biryani '
    dest2.img = " destination_2.jpg "
    dest2.offer = True
    
    dest3 = Destination()
    dest3.name = 'KERALA'
    dest3.price = 700
    dest3.desc = 'Kerala '
    dest3.caps='one of the state of in india and  Beautiful nature'
    dest3.img = " destination_3.jpg "
    dest3.offer = False
    dests =[dest1 ,dest2 , dest3]
    '''
    return render(request, "index1.html",{"dests":dests})
