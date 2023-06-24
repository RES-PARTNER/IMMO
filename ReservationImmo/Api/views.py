# from django.shortcuts import render_to_response
from Api.serializer import (ResidenceSerializers, MediaSerializers,OptionsSerializers,
                            ApartmentOptionSerializers,ApartmentsSerializers,ReviewsSerializers)

from Immobilier.models import Residences,Medias,Options,ApartmentOptions,Reviews,Apartments

from rest_framework import  generics, mixins


# Create your views here.


class ResidenceMixinsViews(generics.GenericAPIView, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                         ):
    
    queryset = Residences.objects.all()
    serializer_class = ResidenceSerializers

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MediaMixinsViews(generics.GenericAPIView, mixins.CreateModelMixin,
                         mixins.UpdateModelMixin, mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                         ):
    
    queryset = Medias.objects.all()
    serializer_class = MediaSerializers

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    

class OptionMixinsViews(generics.GenericAPIView,mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin, ):
    
    queryset = Options.objects.all()
    serializer_class = OptionsSerializers

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class ApartmentOptionMixinsViews(generics.GenericAPIView,mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin, ):
    
    queryset = ApartmentOptions.objects.all()
    serializer_class = ApartmentOptionSerializers

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
class ReviewMixinsViews(generics.GenericAPIView,mixins.CreateModelMixin,
                         mixins.UpdateModelMixin,mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin, ):
    
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializers

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)

        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)