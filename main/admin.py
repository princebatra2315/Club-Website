from django.contrib import admin
from .models import Profile,Event,registration,feedback
# Register your models here.
admin.site.register(Profile)
admin.site.register(Event)
admin.site.register(registration)
admin.site.register(feedback)
