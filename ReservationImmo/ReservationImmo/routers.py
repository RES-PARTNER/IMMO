from rest_framework.routers import DefaultRouter
from Api.viewset import ResidenceViewset,MediaViewset,OptionViewset,ApartmentOptionViewset,ReviewViewset,BookingViewset,ApartmentViewset


router = DefaultRouter()

router.register('residences', ResidenceViewset, basename='residences')
router.register('medias', MediaViewset, basename='medias')
router.register('options', OptionViewset, basename='options')
router.register('apartments', ApartmentViewset, basename='apartments')
router.register('optionapartments', ApartmentOptionViewset, basename='optionapartments')
router.register('reviews', ReviewViewset, basename='reviews')
router.register('bookings', BookingViewset, basename='bookings')



urlpatterns = router.urls