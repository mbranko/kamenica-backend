from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import index, privacy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', index),
    path('/privacy/<str:language>/', privacy),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
