from rest_framework import serializers
from notes.models import Notes

class NotesShowSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields = '__all__'