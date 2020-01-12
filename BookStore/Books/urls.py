from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bookrating',views.BookRatingView)
router.register('books',views.BookView)
router.register('reader',views.BookReaderView)
router.register('rentbook',views.RentBooksView)

urlpatterns = [
    path('',include(router.urls))
]
