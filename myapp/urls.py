from django.urls import path
from .api import BookViewSet
#from .views import


urlpatterns = [
    path(r'api/Book/(?P<slug>[^/.]+)/author_age/(?P<age>\d+)', BookViewSet.as_view({'get': 'author_age'}), name='book-author-age'),
]