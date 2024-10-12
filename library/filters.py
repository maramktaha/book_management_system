import django_filters
from .models import Author





class AuthorFilter(django_filters.FilterSet):
    library=django_filters.NumberFilter(field_name='books',lookup_expr='library')
    category=django_filters.NumberFilter(field_name='books',lookup_expr='category')
    
    class Meta:
        model=Author
        fields=['library','category']
    
 