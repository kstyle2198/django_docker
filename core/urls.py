from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls')),
    path('home/', include('homeapp.urls')),
    path('weather/', include('weatherapp.urls')),
    path('blog/', include('blogapp.urls')),
    path('money/', include('moneyapp.urls')),
    path('dart/', include('dartapp.urls')),
    path('accounts1/', include('loginapp.urls')),
    path('covid/', include('covid.urls')),
    path('dev/', include('devapp.urls')),
    path('accounts/',include('allauth.urls')),
    path('sociallogin/', include('socialloginapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
