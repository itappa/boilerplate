from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("accounts/", include("allauth.urls")),
        path("screenshots/", include("screenshots.urls")),
        path("bookmarks/", include("bookmarks.urls")),
        path("", include("recipes.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
