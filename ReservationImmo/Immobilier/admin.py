from django.contrib import admin

from Immobilier.models import Bookings, Medias, ApartmentOptions, Options, Residences, Reviews,Apartments
from django.utils.html import format_html
# Register your models here.

@admin.register(Residences)
class AdminResidences(admin.ModelAdmin):

    fields = ['title','price','localisation','description']
    list_display=('title','price','localisation','description')
    list_filter = ("title",'localisation','price', )
    search_fields = ("title__startswith",'localisation__startswith','price__startswith')
    list_per_page = 2

    
class AdminMedias(admin.ModelAdmin):
    
    def image_media(self, obj):
        return format_html(f"<img src='/MEDIA/{obj.image}' width='50px' hieght='50px' />")
    image_media.short_description = 'MODEL CHOISIE'
    # image_catalogallow_tags = True

    list_display=('image_media', 'residence')

class AdminOptions(admin.ModelAdmin):
     list_display=('name',)

class AdminApartments(admin.ModelAdmin):
    list_display=('residence', 'apartmentNumber','pieceNumber', 'bathroomNumber','bedNumber')

class AdminApartmentOptions(admin.ModelAdmin):
    list_display=('apartment', 'option','description')

class AdminReviews(admin.ModelAdmin):
    fields = ['residence','rating','user','comments']
    list_display=('residence','rating','user','comments')

class AdminBookings(admin.ModelAdmin):
    list_display=('startDate', 'endDate','residence','user')

# admin.site.register(Residences, AdminResidences)
admin.site.register(Medias, AdminMedias)
admin.site.register(Options, AdminOptions)
admin.site.register(Apartments, AdminApartments)
admin.site.register(ApartmentOptions, AdminApartmentOptions)
admin.site.register(Reviews, AdminReviews)
admin.site.register(Bookings, AdminBookings)