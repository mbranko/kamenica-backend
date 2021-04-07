from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index, privacy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('privacy/<str:language>/', privacy),
    path('', index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
