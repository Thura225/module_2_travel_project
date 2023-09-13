from django.shortcuts import render,redirect
from .models import Bus,POINT
from .forms import BusForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

def buseslist(request):
    if request.method == 'GET':
        buses = Bus.objects.all()
        return render(request,'buses.html',{'buses':buses,'points':POINT})
    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')
        filter_buses = Bus.objects.filter(start_point=start,end_point = end)
        return render(request,'buses.html',{'buses':filter_buses,'points':POINT})
    

@permission_required('buses.add_buses',login_url='error')
def busescreate(request):
    form = BusForm()
    if request.method == "POST":
        form = BusForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/buses/')
    return render(request,'buscreate.html',{"form":form})

@permission_required('buses.change_buses',login_url='error')
def busesupdate(request,bus_id):
    bus = Bus.objects.get(id=bus_id)
    if request.method == "POST":
        bus_name = request.POST.get("bus_name")
        start_point = request.POST.get("start_point")
        end_point = request.POST.get("end_point")
        price = request.POST.get("price")
        deperture_date = request.POST.get("deperture_date")

        bus.name = bus_name
        bus.start_point = start_point
        bus.end_point = end_point
        bus.price = price
        bus.deperture_date = deperture_date
        bus.save()
        return redirect('/buses/')
    return render(request,'busupdate.html',{"points":POINT,"bus":bus})

@permission_required('buses.delete_buses',login_url='error')
def busesdelete(request,bus_id):
    bus = Bus.objects.get(id=bus_id)
    bus.delete()
    return redirect('/buses/')