
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.sttic import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pages.urls")),
]


urlpatterns += static(settings.MEDI_URL, document_root=settings.MEDIA_ROOT)