from django.urls import path
from .views import index, top_sellers, advertisement_post, adv_detali


urlpatterns = [
    path('', index, name="main-page"),
    path('top-sellers/', top_sellers, name="sellers"),
    path('advertisement/', advertisement_post, name='advert_post'),
    path('advertisement/<int:pk>', adv_detali, name="adv_detali")
]