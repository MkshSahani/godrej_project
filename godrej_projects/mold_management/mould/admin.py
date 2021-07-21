from django.contrib import admin
from .models import Mould, MouldStatus

admin.site.register(Mould) # register Mould Model. 
admin.site.register(MouldStatus)