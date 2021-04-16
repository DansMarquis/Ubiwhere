from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Occurrence
from datetime import datetime
from .models import Occurrence

@admin.register(Occurrence)
class OccurrenceAdmin(OSMGeoAdmin):
    
    # Makes sense for the admin to update only the state
    #readonly_fields = ["description", "author", "location", "creationDate", "updateDate", "category"]
    
    # Update Date based on State changes
    def save_model(self, request, obj, form, change):
        if request.user.username == 'admin':
            obj.updateDate = datetime.now()
        else:
            obj.author = request.user.username
        super().save_model(request, obj, form, change)
        
    
    