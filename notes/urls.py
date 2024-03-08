
from django.urls import path
from notes import views
urlpatterns = [
    path('create/',views.create_note),
    path('update/',views.update_note),
    path('delete/',views.delete_note)
]
