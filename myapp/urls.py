from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('', views.home, name='home'),

    path('add/', views.add_student, name='add_student'),

    path('update/<int:id>/', views.update_student, name='update_student'),

    path('delete/<int:id>/', views.delete_student, name='delete_student'),

    path('api/', views.student_api, name='student_api'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]