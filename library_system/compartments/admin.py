from django.contrib import admin
from .models import Compartment, Student, OTP

# Register your models here.
admin.site.register(Compartment)
admin.site.register(Student)
admin.site.register(OTP)
