from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import custom_404

handler404 = custom_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
