from django.contrib import admin
from django.contrib.gis import admin as gadmin
from .models import User,Customer,Librarian

admin.site.register(User, gadmin.GISModelAdmin,list_display=['id','first_name','last_name','email'])
admin.site.register(Customer)
admin.site.register(Librarian)
