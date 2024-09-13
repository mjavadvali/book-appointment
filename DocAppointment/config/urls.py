from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('appointment.urls')),
    path('api/authentication/', include('dj_rest_auth.urls')),
    path('authentication/', include('accounts.urls'))
]
