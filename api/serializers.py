from django.db.models import fields
from .models import Occurrence
from rest_framework import serializers
class OccurrenceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Occurrence
        read_only_fields = ["state","author", "creationDate", "updateDate"]
        fields='__all__'
        
