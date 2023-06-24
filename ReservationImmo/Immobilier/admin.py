from django.contrib import admin

from Immobilier.models import Bookings, Medias, ApartmentOptions, Options, Residences, Reviews,Apartments

# Register your models here.

class AdminResidences(admin.ModelAdmin):

    list_display=('title', 'description', 'localisation', 'price')

class AdminMedias(admin.ModelAdmin):
    list_display=('image', 'residence')
    

class AdminOptions(admin.ModelAdmin):
     list_display=('name',)

class AdminApartments(admin.ModelAdmin):
    list_display=('residence', 'apartmentNumber','pieceNumber', 'bathroomNumber','bedNumber')

class AdminApartmentOptions(admin.ModelAdmin):
    list_display=('apartment', 'option','description')

class AdminReviews(admin.ModelAdmin):
    list_display=('comments', 'rating','residence','user')

class AdminBookings(admin.ModelAdmin):
    list_display=('startDate', 'endDate','residence','user')

admin.site.register(Residences, AdminResidences)
admin.site.register(Medias, AdminMedias)
admin.site.register(Options, AdminOptions)
admin.site.register(Apartments, AdminApartments)
admin.site.register(ApartmentOptions, AdminApartmentOptions)
admin.site.register(Reviews, AdminReviews)
admin.site.register(Bookings, AdminBookings)