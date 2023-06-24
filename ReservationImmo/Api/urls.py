from django.urls import path

from .views import ResidenceMixinsViews,MediaMixinsViews,OptionMixinsViews,ApartmentOptionMixinsViews,ReviewMixinsViews





urlpatterns = [
    # Residances
    path('residence/',ResidenceMixinsViews.as_view() ),
    path('detail/<str:pk>/',ResidenceMixinsViews.as_view() ),
    path('create/',ResidenceMixinsViews.as_view() ),
    path('update/<str:pk>/',ResidenceMixinsViews.as_view() ),
    path('delete/<str:pk>/',ResidenceMixinsViews.as_view() ),

    # Media
    path('media/',MediaMixinsViews.as_view() ),
    path('option/',OptionMixinsViews.as_view() ),
    path('optionResidence/',ApartmentOptionMixinsViews.as_view() ),
    path('review/',ReviewMixinsViews.as_view() ),

]