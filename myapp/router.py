from rest_framework import routers
from .api import AuthorViewSet, BookViewSet


#from .views import

router = routers.DefaultRouter()
router.register('api/Author', AuthorViewSet, 'author')
router.register('api/Book', BookViewSet, 'book')

urlpatterns = router.urls