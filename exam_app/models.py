from django.db import models
from login_app.models import User
from datetime import datetime

class TripManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['trip_destination']) <= 0:
            errors['trip_destination'] = "Destination must be at a minimum of 3 characters!"

        if len(post_data['trip_start_date']) <= 0:
            errors['trip_start_date'] = "Please provide a start date!"

        if len(post_data['trip_end_date']) <= 0:
            errors['trip_end_date'] = "Please provide an end date!"

        if len(post_data['trip_plan']) <= 0:
            errors['trip_plan'] = "Plan must be a minimum of 3 characters!"
        if len(post_data['trip_start_date']) != 10:
            errors['trip_start_date'] = "Please provide a valid date!"
        else:
            form_date = datetime.strptime(post_data['trip_start_date'], "%Y-%m-%d")
        if len(post_data['trip_end_date']) != 10:
            errors['trip_end_date'] = "Please provide a valid date!"
        else:
            form_date = datetime.strptime(post_data['trip_end_date'], "%Y-%m-%d")

        return errors

class Trip(models.Model):
    destination = models.CharField(max_length = 100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    plan = models.TextField(max_length = 500)
    admin = models.ForeignKey(
        User, related_name="trips_created", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = TripManager()
