from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListApi, BookDetailApiView, BookDeleteApiView, \
    BookUpdateApiView, BookCreateApiView,BookListCreate,BookViewset

router = SimpleRouter()
router.register('books', BookViewset, basename='books')

urlpatterns = [

]

urlpatterns += router.urls
