from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import BuildJob, BuildRun, Environment, Deployment


def dashboard_overview(request):
    """Main dashboard view showing overview of all jobs and recent activity"""
    
    # Get all active jobs with their latest builds
    jobs = BuildJob.objects.filter(status='active').prefetch_related('build_runs')
    
    # Get recent build activity (last 24 hours)
    recent_builds = BuildRun.objects.filter(
        started_at__gte=timezone.now() - timedelta(hours=24)
    ).select_related('job')[:10]
    
    # Get deployment status for all environments
    environments = Environment.objects.filter(is_active=True).prefetch_related('deployments')
    
    # Calculate statistics
    total_jobs = jobs.count()
    running_builds = BuildRun.objects.filter(status__in=['pending', 'running']).count()
    failed_builds_today = BuildRun.objects.filter(
        started_at__gte=timezone.now().replace(hour=0, minute=0, second=0),
        status='failed'
    ).count()
    
    # Success rate calculation
    builds_today = BuildRun.objects.filter(
        started_at__gte=timezone.now().replace(hour=0, minute=0, second=0)
    )
    success_rate = 0
    if builds_today.exists():
        successful_today = builds_today.filter(status='success').count()
        success_rate = (successful_today / builds_today.count()) * 100
    
    context = {
        'jobs': jobs,
        'recent_builds': recent_builds,
        'environments': environments,
        'stats': {
            'total_jobs': total_jobs,
            'running_builds': running_builds,
            'failed_builds_today': failed_builds_today,
            'success_rate': round(success_rate, 1),
        }
    }
    
    return render(request, 'dashboard/overview.html', context)


def job_detail(request, job_id):
    """Detailed view of a specific job and its build history"""
    
    job = get_object_or_404(BuildJob, id=job_id)
    builds = job.build_runs.all()[:20]  # Last 20 builds
    
    # Get deployment history for this job's builds
    deployments = Deployment.objects.filter(
        build_run__job=job
    ).select_related('environment', 'build_run')[:10]
    
    context = {
        'job': job,
        'builds': builds,
        'deployments': deployments,
    }
    
    return render(request, 'dashboard/job_detail.html', context)


def build_detail(request, build_id):
    """Detailed view of a specific build run"""
    
    build = get_object_or_404(BuildRun, id=build_id)
    deployments = build.deployments.all().select_related('environment')
    
    context = {
        'build': build,
        'deployments': deployments,
    }
    
    return render(request, 'dashboard/build_detail.html', context)


def environments_view(request):
    """View showing all environments and their deployment status"""
    
    environments = Environment.objects.filter(is_active=True)
    
    # Get latest deployment for each environment
    env_data = []
    for env in environments:
        latest_deployment = env.deployments.first()
        env_data.append({
            'environment': env,
            'latest_deployment': latest_deployment,
        })
    
    context = {
        'env_data': env_data,
    }
    
    return render(request, 'dashboard/environments.html', context)


def api_job_status(request, job_id):
    """API endpoint to get current job status (for AJAX updates)"""
    
    job = get_object_or_404(BuildJob, id=job_id)
    latest_build = job.latest_build
    
    data = {
        'job_name': job.name,
        'status': job.status,
        'latest_build': None,
    }
    
    if latest_build:
        data['latest_build'] = {
            'build_number': latest_build.build_number,
            'status': latest_build.status,
            'started_at': latest_build.started_at.isoformat(),
            'duration': latest_build.duration_display,
        }
    
    return JsonResponse(data)


def api_build_log(request, build_id):
    """API endpoint to get build log output"""
    
    build = get_object_or_404(BuildRun, id=build_id)
    
    data = {
        'build_number': build.build_number,
        'job_name': build.job.name,
        'status': build.status,
        'log_output': build.log_output or 'No log output available.',
    }
    
    return JsonResponse(data)

