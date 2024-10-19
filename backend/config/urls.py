from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token_view(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})

urlpatterns = [
    path('csrf-token/', csrf_token_view, name='csrf_token_view'),
    
    path('admin/', admin.site.urls),
    path("", include('appointment.urls')),
    path('accounts/', include('accounts.urls')),
    path("api-auth/", include("rest_framework.urls")),

    path('api/authentication/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    