from django.contrib import admin
from .models import Dog
from .models import Breed

class DogAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'breed', 'gender')
    
    # Add search functionality for specific fields
    search_fields = ('name', 'breed')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('age', 'breed', 'gender')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('name', 'age', 'breed', 'gender', 'color', 'favoritetoy', 'favoritefood')

class BreedAdmin(admin.ModelAdmin):
        # Define the list of fields to display in the admin interface
    list_display = ('breed', 'size')
    
    # Add search functionality for specific fields
    search_fields = ('breed', 'size')

    # Add filters for the age and breed fields in the sidebar
    list_filter = ('size',)

    # Define which fields can be clicked to view the details page
    list_display_links = ('breed',)

    # Define how fields are displayed when editing a Dog instance
    fields = ('breed', 'size', 'friendliness', 'trainability', 'sheddingamount', 'excerciseneeds')

# Register the model and admin class
admin.site.register(Dog, DogAdmin)
admin.site.register(Breed, BreedAdmin)