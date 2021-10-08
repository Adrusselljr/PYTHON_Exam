from django.urls import path
from . import views

urlpatterns = [
    path('trips', views.trips),
    path('trips/new', views.new_trip),
    path('trips/create', views.create_trip),
    path('trips/<int:trip_id>', views.trip_info),
    path('trips/<int:trip_id>/edit', views.edit_trip),
    path('trips/<int:trip_id>/update', views.update_trip),
    path('users/logout', views.logout),
    path('trips/<int:trip_id>/remove', views.remove_trip)
]
