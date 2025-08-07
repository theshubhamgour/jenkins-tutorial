from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Main dashboard views
    path('', views.dashboard_overview, name='overview'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('build/<int:build_id>/', views.build_detail, name='build_detail'),
    path('environments/', views.environments_view, name='environments'),
    
    # API endpoints
    path('api/job/<int:job_id>/status/', views.api_job_status, name='api_job_status'),
    path('api/build/<int:build_id>/log/', views.api_build_log, name='api_build_log'),
]

