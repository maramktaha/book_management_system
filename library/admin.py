from django.contrib import admin

# Register your models here.
from .models import Library,Book,Author,Category,LibraryTransaction,BorrowReturnBook

from django.contrib.gis import admin as gadmin
from modeltranslation.admin import TranslationAdmin


admin.site.register(Book,list_displau=['id','name'])
admin.site.register(Author,list_displau=['id','name'])
admin.site.register(LibraryTransaction)
admin.site.register(BorrowReturnBook)



class LibraryAdmin(TranslationAdmin,gadmin.GISModelAdmin):
    pass

admin.site.register(Library, LibraryAdmin)

class CategoryAdmin(TranslationAdmin):
    pass

admin.site.register(Category, CategoryAdmin)