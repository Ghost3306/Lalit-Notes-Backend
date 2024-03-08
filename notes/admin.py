from django.contrib import admin
from notes.models import Notes
# Register your models here.
class DisplayNotes(admin.ModelAdmin):
    list_display=('title','note','user','datetime')

admin.site.register(Notes,DisplayNotes)