from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views as main_views

handler404 = main_views.custom_404
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('devices/', include('devices.urls')),
    path('users/', include('users.urls')),
    path('panel/', include('panel.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug/__', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)