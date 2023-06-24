
from Immobilier.models import Residences,Medias,Options,ApartmentOptions,Reviews,Bookings,Apartments
from rest_framework import serializers
from rest_framework.reverse import reverse

from django.contrib.auth import get_user_model
User = get_user_model()



 #serealiser product    
class ResidenceSerializers(serializers.ModelSerializer):

     id = serializers.IntegerField(read_only=True)
     title = serializers.CharField()
     description = serializers.CharField()
     localisation = serializers.CharField()
     price = serializers.FloatField()

     class Meta:
          model =Residences
          fields = ('id','title', 'description','localisation','price')

     # def get_my_discount(self, obj):
     #      if not hasattr(obj, 'id'):
     #           return None
     #      if not isinstance(obj, Residences):
     #           return None
     #      return obj.get_discount  

class MediaSerializers(serializers.ModelSerializer):

     id = serializers.IntegerField(read_only=True)
     image = serializers.ImageField()
     residence = serializers.PrimaryKeyRelatedField(queryset=Residences.objects.all())
    
     class Meta:
          model =Medias
          fields = ('id','image', 'residence')
    

class OptionsSerializers(serializers.ModelSerializer):

     id = serializers.CharField(read_only=True)
     name = serializers.CharField()

     class Meta:
          model =Options
          fields = ('id','name')
class ApartmentsSerializers(serializers.ModelSerializer):

     id = serializers.CharField(read_only=True)
     apartmentNumber = serializers.CharField()
     pieceNumber = serializers.IntegerField()
     bathroomNumber = serializers.IntegerField()
     bedNumber = serializers.IntegerField()
     residence = serializers.PrimaryKeyRelatedField(queryset=Residences.objects.all())

     class Meta:
          model =Apartments
          fields = ('id','apartmentNumber','pieceNumber','bathroomNumber','bedNumber','residence')

class ApartmentOptionSerializers(serializers.ModelSerializer):

     id = serializers.CharField(read_only=True)
     apartment = serializers.PrimaryKeyRelatedField(queryset=Apartments.objects.all())
     option = serializers.PrimaryKeyRelatedField(queryset=Options.objects.all())
     description = serializers.CharField()

     class Meta:
          model =ApartmentOptions
          fields = ('id','apartment','option', 'description')

class ReviewsSerializers(serializers.ModelSerializer):

     id = serializers.CharField(read_only=True)
     residence = serializers.PrimaryKeyRelatedField(queryset=Residences.objects.all())
     user = serializers.PrimaryKeyRelatedField(queryset= User.objects.all())
     rating = serializers.IntegerField()
     comments = serializers.CharField()

     class Meta:
          model =Reviews
          fields = ('id','residence','user', 'rating','comments')

class BookingSerializers(serializers.ModelSerializer):

     id = serializers.CharField(read_only=True)
     residence = serializers.PrimaryKeyRelatedField(queryset=Residences.objects.all())
     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
     statut = serializers.CharField()
     startDate = serializers.DateField()
     endDate = serializers.DateField()

     class Meta:
          model =Bookings
          fields = ('id','residence','user', 'statut','startDate','endDate')


     
