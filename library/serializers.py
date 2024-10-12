from rest_framework import serializers
from .models import (
    Library,
    Book,
    Author,
    Category,
    LibraryTransaction,
    BorrowReturnBook,
    Branch,
)
from django.db.models.signals import post_save,m2m_changed
from django.db import transaction
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ("name", "id")


class BookSerializer(serializers.ModelSerializer):
    category_object = CategorySerializer(read_only=True, source="category")
    author_name = serializers.ReadOnlyField(source="author.name")

    class Meta:
        model = Book
        fields = "__all__"
        extra_kwargs = {
            "category": {"write_only": True},
            "author": {"write_only": True},
        }


class AuthorSerializer(serializers.ModelSerializer):
    books_count = serializers.ReadOnlyField()
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class LibrarySerializer(serializers.ModelSerializer):
    books_list = BookSerializer(many=True, read_only=True, source="books")
    branches_list=BranchSerializer(many=True,read_only=True,source='branches')
    class Meta:
        model = Library
        exclude = ("name_ar", "name_en")
        extra_kwargs = {"books": {"write_only": True}}


class BorrowReturnBookSerializer(serializers.Serializer):
    books = serializers.PrimaryKeyRelatedField(many=True, queryset=Book.objects.all())
   


class BorrowReturrnBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BorrowReturnBook
        fields='__all__'
        extra_kwargs={'transaction':{'read_only':True}}
        
        
class LibraryTransactionSerializer(serializers.ModelSerializer):
    books=BorrowReturrnBookSerializer(many=True,source='books_transactions')
   

    class Meta:
        model = LibraryTransaction
        fields = "__all__"
        extra_kwargs={'librarian':{'read_only':True}}
    @transaction.atomic   
    def create(self, validated_data):
        books=validated_data.pop('books_transactions',[])
        instance= super().create(validated_data)
        borrowed_books=[]
        if books:
            for book in books:
                borrowed_book = BorrowReturnBook(transaction=instance, **book)
                borrowed_book.clean() 
                borrowed_books.append(borrowed_book)
    
        if borrowed_books:
            # Dispatch the 'pre_add' m2m_changed signal manually
            m2m_changed.send(
                sender=LibraryTransaction.books.through,  # Through model of M2M relationship
                instance=instance,
                action='pre_add',  # You want to mimic the 'pre_add' action
                reverse=False,
                model=Book,
                pk_set={book.book.pk for book in borrowed_books},  # Set of book IDs being added
                using='default',
            )
        BorrowReturnBook.objects.bulk_create(borrowed_books)
        
    
        
        return instance
                
            
