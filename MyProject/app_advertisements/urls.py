from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('index/', index, name='index'),
    path('advertisement-post/', advertisement_post, name='adv-post'),
    path('advertisement/', advertisement, name='advertisement'),
]
