from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.sitemaps.views import sitemap
from home.sitemaps import StaticViewSitemap


sitemaps = {
    'static': StaticViewSitemap
}



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('product/', include('products.urls')),
    path('accounts/', include('accounts.urls')),
    path("accounts/", include("allauth.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
