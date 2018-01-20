from django.conf.urls import url
from . import views # . znamená aktuální adresář

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # '^$' = regulární výraz, způsob, jak hledat řetězce; řetězce, které v sobě mají a -> 'a*', ^ znamená začátek, $ znamená konec
]
