from django.shortcuts import render,redirect
from .models import Bookings
from buses.models import Bus
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def bookinglists(request):
    bookings = Bookings.objects.all()
    return render(request,'bookings.html',{'bookings':bookings})

@login_required(login_url='login')
def bookingdelete(request,book_id):
    booking = Bookings.objects.get(id=book_id)
    booking.delete()
    return redirect('/bookings/')

@login_required(login_url='login')
def bookingcreate(request,bus_id):
    if request.method == 'GET':
        bus = Bus.objects.get(id=bus_id)
        return render(request,'bookingscreate.html',{'bus':bus})
    if request.method == 'POST':
        person = request.POST.get('person')
        credit = request.POST.get('credit')
        Bookings.objects.create(
            bus_id=bus_id,
            buyer_id=request.user.id,
            people = person,
            credit_card = credit
            )
        
        return redirect('/bookings/')