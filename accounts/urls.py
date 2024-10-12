
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterUser,Profile,CustomersModelViewSet,LibrarianModelViewSet
from rest_framework import routers

router=routers.DefaultRouter()

router.register("customers",CustomersModelViewSet)
router.register("librarians",LibrarianModelViewSet)


urlpatterns = [

    
 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterUser.as_view()),
    path('profile/',Profile.as_view()),
    path('',include(router.urls))
    

]
