from django.urls import path, include
from .views import book_list


urlpatterns = [
    path('', book_list, name='book_list'),
    path('lang/set/', include('django.conf.urls.i18n'))
]