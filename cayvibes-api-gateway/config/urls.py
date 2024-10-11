from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from views import ProxyView

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/auth/', include('core.urls')),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
=======
    path('api/', include('core.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
>>>>>>> d0568b6 (adding files)
    re_path(r'^api/auth/', include('drf_social_oauth2.urls', namespace='drf')),
]

# JWT token endpoints
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns += [
    re_path(r'^api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
<<<<<<< HEAD
    re_path(r'^(?P<service_name>\w+)/(?P<path>.*)$', ProxyView.as_view(), name='proxy')
=======
    re_path(r'^api/(?P<service_name>\w+)/(?P<path>.*)$', ProxyView.as_view(), name='proxy')
>>>>>>> d0568b6 (adding files)
]
