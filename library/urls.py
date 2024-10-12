from django.urls import path,include


from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register('libraries',LibraryView)
router.register('categories',CategoryView)
router.register('authors',AuthorView)

router.register('books',BookView)
router.register('branches',BranchView)
router.register('transactions',LibraryTransactionView)



urlpatterns = [

    
    path('',include(router.urls))

]
