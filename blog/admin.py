from django.contrib import admin
from .models import Post # tečka na začátku -> importuje se to ze stejného adresáře, ve kterém jsme, tzn. blog.models

# Register your models here.

admin.site.register(Post)
