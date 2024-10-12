from .models import *
from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        exclude=('is_staff','last_login','is_active','user_permissions')
        extra_kwargs={'password':{"write_only":True}}
 
        
class CustomerSerializer(UserSerializer):
    nearby_librarries=serializers.SerializerMethodField()
    borrowed_books_count=serializers.SerializerMethodField()
    
    def get_nearby_librarries(self,obj):
        return obj.get_nearby_libraries()
    
    def get_borrowed_books_count(self,obj):
        return obj.get_borrowed_books_count()
    
class LibrarianSerializer(UserSerializer):
    pass