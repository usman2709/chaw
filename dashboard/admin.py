from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [ 'id','user', 'first_name','last_name', 'email', 'phone', 'address','city', 'state', 'profile_pix']
    list_editable = ['user', 'first_name','last_name', 'email', 'phone', 'address','city', 'state']
