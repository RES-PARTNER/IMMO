import uuid
from django.conf import settings
from django.db import models
from django.utils.html import mark_safe

User =settings.AUTH_USER_MODEL

class Residences(models.Model):
    uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    title = models.fields.CharField(max_length=100)
    description = models.fields.TextField(blank=True, null=True)
    localisation = models.fields.CharField(max_length=100)
    price = models.fields.FloatField(default=0)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}  {self.price }"

class Medias(models.Model):
     uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
     image = models.ImageField(upload_to="media" , blank=True, null=True)
     residence =models.ForeignKey(Residences, on_delete=models.CASCADE)
     created_at = models.fields.DateTimeField(auto_now_add=True)
     updated_at = models.fields.DateTimeField(auto_now_add=True)

     def image_tag(self):
        return mark_safe('<img src="MEDIA/%s" width="100px" height="100px" />'%(self.image.url))
     image_tag.short_description = 'Image'

class Options(models.Model):
     uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
     name = models.fields.CharField(max_length=200)
     created_at = models.fields.DateTimeField(auto_now_add=True)
     updated_at = models.fields.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f"{self.name}"

class Apartments(models.Model):
    uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    apartmentNumber = models.CharField( max_length=45)
    pieceNumber = models.fields.IntegerField()
    bathroomNumber = models.fields.IntegerField()
    bedNumber = models.fields.IntegerField()
    residence =models.ForeignKey(Residences, on_delete=models.CASCADE)
    created_at = models.fields.DateTimeField(auto_now_add=True)
    updated_at = models.fields.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.residence} {self.apartmentNumber}"

    

class ApartmentOptions(models.Model):
     uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
     apartment =models.ForeignKey(Apartments, on_delete=models.CASCADE)
     option =models.ForeignKey(Options, on_delete=models.CASCADE)
     description = models.fields.TextField(blank=True, null=True)
     created_at = models.fields.DateTimeField(auto_now_add=True)
     updated_at = models.fields.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f"{self.apartment}  {self.option}"
     

class Reviews(models.Model):
     uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
     comments = models.fields.TextField(blank=True, null=True)
     rating = models.fields.IntegerField()
     residence =models.ForeignKey(Residences, on_delete=models.CASCADE)
     user =models.ForeignKey(User, on_delete=models.CASCADE)
     created_at = models.fields.DateTimeField(auto_now_add=True)
     updated_at = models.fields.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f"{self.residence}  {self.rating}"
     
class Bookings(models.Model):
     uuid  = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
     startDate = models.fields.DateField(blank=True, null=True)
     endDate = models.fields.DateField(blank=True, null=True)
     statut = models.fields.CharField(max_length=45)
     residence =models.ForeignKey(Residences, on_delete=models.CASCADE)
     user =models.ForeignKey(User, on_delete=models.CASCADE)
     created_at = models.fields.DateTimeField(auto_now_add=True)
     updated_at = models.fields.DateTimeField(auto_now_add=True)

     def __str__(self):
        return f"{self.startDate}  {self.residence}"
