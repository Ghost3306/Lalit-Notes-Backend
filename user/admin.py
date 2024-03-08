from django.contrib import admin
from user.models import Users

class DisplayUser(admin.ModelAdmin):
    list_display=('username','password')

admin.site.register(Users,DisplayUser)