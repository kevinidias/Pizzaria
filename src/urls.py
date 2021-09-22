from django.contrib import admin
from django.db.models import base
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pizzaria.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
