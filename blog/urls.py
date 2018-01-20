from django.conf.urls import url
from . import views # . znamená aktuální adresář

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'), # '^$' = regulární výraz, způsob, jak hledat řetězce; řetězce, které v sobě mají a -> 'a*', ^ znamená začátek, $ znamená konec
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]
