from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CoockingWebsite.index.urls')),
    path('accounts/', include('CoockingWebsite.accounts.urls')),
    path('posts/', include('CoockingWebsite.posts.urls')),
    path('dashboard/', include('CoockingWebsite.dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)