from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, CreateAPIView
from .models import *
from .serializers import UserSerializer, CustomerSerializer, LibrarianSerializer
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from .permissions import IsLibrarian

class RegisterUser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class Profile(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class CustomersModelViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsLibrarian]


class LibrarianModelViewSet(ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer
    permission_classes = [IsAdminUser]
