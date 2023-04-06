from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('store/', include('store.urls')),
    # path('category/', include('category.urls')),
]
