from django.shortcuts import render
from .serializers import (
    LibrarySerializer,
    AuthorSerializer,
    CategorySerializer,
    BookSerializer,
    LibraryTransactionSerializer,
    BorrowReturnBookSerializer,
    BranchSerializer
)
from accounts.permissions import IsLibrarian
from rest_framework.viewsets import ModelViewSet
from .models import Book, Library, Author, Category, LibraryTransaction,Branch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .filters import *
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
class BranchView(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
  



class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ["category", "author",'library']
   


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class=AuthorFilter
    permission_classes=[IsLibrarian]


class LibraryView(ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["books__category", "books__author"]
    permission_classes=[IsAuthenticatedOrReadOnly]


class LibraryTransactionView(ModelViewSet):
    queryset=LibraryTransaction.objects.all()
    serializer_class=LibraryTransactionSerializer
    permission_classes=[IsLibrarian]
    
    def perform_create(self, serializer):
        return serializer.save(librarian=self.request.user.librarian)
    
    @action(detail=True,methods=['post'],serializer_class=BorrowReturnBookSerializer)
    def return_books(self,request,*args,**kwargs):
        
        today=timezone.now()
        object=self.get_object()
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        books=serializer.validated_data['books']
        object.name='return'
        object.save()
      
        for borrowed_book in object.books_transactions.all():
            if borrowed_book.book in books:

                if borrowed_book.return_date < today:
            
                    borrowed_book.penalty= (today-borrowed_book.return_date).days *5
            
                borrowed_book.is_returned=True
              
                borrowed_book.book.is_available=True
                borrowed_book.book.save()
                borrowed_book.save()
                channel_layer = get_channel_layer()
                async_to_sync(channel_layer.group_send)(
                    "book_notifications", 
                    {
                        "type": "send_book_notification",
                        "message": f"A book with id {borrowed_book.book.id} and title {borrowed_book.book.title} has been returned and is now available."
                    }
                )
                
            
       
        return Response({'message':"transaction done successfully"})
            
    