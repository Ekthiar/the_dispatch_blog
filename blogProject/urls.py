
from django.contrib import admin
from django.urls import path, include
from  home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name = 'home'),
    path('author/', include('authors.urls')),
    path('categorie/', include('categories.urls')),
    path('post/', include('posts.urls')),
    path('profile/', include('profiles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
