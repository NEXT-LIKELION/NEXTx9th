from django.contrib import admin
from .models import Event, Fotd,Ootd,Totd,Motd,Profile
# from .calendar import Calendar
# from .forms import EventForm

# Register your models here.
admin.site.register(Fotd)
admin.site.register(Ootd)
admin.site.register(Totd)
admin.site.register(Motd)
admin.site.register(Profile)
# admin.site.register(Event)
# admin.site.register(Calendar)
# admin.site.register(EventForm)