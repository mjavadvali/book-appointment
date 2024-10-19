from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    path('get_user_pk/', views.get_user_pk, name='get_user_pk'),
    path('get_user_info/', views.get_user_info, name='get_user_info'),
    path('reset_email/', views.reset_email, name='reset_email')
]
