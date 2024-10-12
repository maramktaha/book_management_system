from modeltranslation.translator import translator, TranslationOptions
from .models import Library,Category

class LibraryTranslationOptions(TranslationOptions):
    fields = ('name', )


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )
translator.register(Library, LibraryTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
