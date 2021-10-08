from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_app.models import User
from .models import Trip

def trips(request):
    if not 'user_id' in request.session:
        messages.error(request, "Log in to view this page!")
    context = {
        "trips": Trip.objects.all(),
        "user": User.objects.get(id = request.session['user_id'])
    }
    return render(request, "trips.html", context)

def new_trip(request):
    return render(request, "new_trip.html")

def create_trip(request):
    errors = Trip.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/trips/new')
    Trip.objects.create(
        destination = request.POST['trip_destination'],
        start_date = request.POST['trip_start_date'],
        end_date = request.POST['trip_end_date'],
        plan = request.POST['trip_plan'],
        admin = User.objects.get(id = request.session['user_id'])
    )
    return redirect('/trips')

def trip_info(request, trip_id):
    context = {
    'trip': Trip.objects.get(id = trip_id),
    'user': User.objects.get(id = request.session['user_id'])
    }
    return render(request, "trip_info.html", context)

def edit_trip(request, trip_id):
    user = User.objects.get(id = request.session['user_id'])
    trip = Trip.objects.get(id = trip_id)
    if user != trip.admin:
        messages.error(request, "Must be Admin to edit this information!")
        return redirect('/trips')
    context = {
        'trip' : trip
    }
    return render(request, "edit_trip.html", context)

def update_trip(request, trip_id):
    user = User.objects.get(id = request.session['user_id'])
    trip = Trip.objects.get(id = trip_id)
    if user != trip.admin:
        messages.error(request, "Must be Admin to edit this information!")
        return redirect('/trips')

    errors = Trip.objects.basic_validator(request.POST)
    if errors:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect(f'/trips/{trip_id}/edit')

    trip.destination = request.POST['trip_destination']
    trip.start_date = request.POST['trip_start_date']
    trip.end_date = request.POST['trip_end_date']
    trip.plan = request.POST['trip_plan']
    trip.save()
    return redirect('/trips')

def logout(request):
    request.session.clear()
    return redirect('/')

def remove_trip(request, trip_id):
    user = User.objects.get(id = request.session['user_id'])
    trip = Trip.objects.get(id = trip_id)
    if user != trip.admin:
        messages.error(request, "Must be Admin to remove this trip!")
        return redirect('/trips')
    trip = Trip.objects.get(id = trip_id).delete()
    messages.info(request, "You deleted the trip!")
    return redirect('/trips')
