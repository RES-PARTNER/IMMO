from Immobilier.models import Residences,Medias,Options,ApartmentOptions,Reviews,Bookings,Apartments
from .serializer import (ResidenceSerializers,MediaSerializers,OptionsSerializers,ApartmentOptionSerializers,
                         BookingSerializers,ReviewsSerializers,ApartmentsSerializers)

from rest_framework import mixins, viewsets



class ResidenceViewset(viewsets.ModelViewSet):
   
    """
    get -> list -> QuerySet  get -> retrieve post -> create put -> update patch ->partial update delete -> destroy
    """ 
    queryset = Residences.objects.all()
    serializer_class = ResidenceSerializers

class MediaViewset(viewsets.ModelViewSet):
  
    queryset = Medias.objects.all()
    serializer_class = MediaSerializers

class OptionViewset(viewsets.ModelViewSet):
  
    queryset = Options.objects.all()
    serializer_class = OptionsSerializers

class ApartmentViewset(viewsets.ModelViewSet):
  
    queryset = Apartments.objects.all()
    serializer_class = ApartmentsSerializers
    
class ApartmentOptionViewset(viewsets.ModelViewSet):
  
    queryset = ApartmentOptions.objects.all()
    serializer_class = ApartmentOptionSerializers
    
class ReviewViewset(viewsets.ModelViewSet):
  
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

class BookingViewset(viewsets.ModelViewSet):
  
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializers