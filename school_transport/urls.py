from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'transport.views.error_404'
handler500 = 'transport.views.error_500'
handler403 = 'transport.views.error_403'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transport.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
