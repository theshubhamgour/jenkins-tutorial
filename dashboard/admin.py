from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import BuildJob, BuildRun, Environment, Deployment


@admin.register(BuildJob)
class BuildJobAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'branch', 'latest_build_status', 'success_rate_display', 'created_at']
    list_filter = ['status', 'branch', 'created_at']
    search_fields = ['name', 'description', 'repository_url']
    readonly_fields = ['created_at', 'updated_at', 'latest_build_info']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'status')
        }),
        ('Repository Settings', {
            'fields': ('repository_url', 'branch')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
        ('Build Information', {
            'fields': ('latest_build_info',),
            'classes': ('collapse',)
        }),
    )
    
    def latest_build_status(self, obj):
        latest = obj.latest_build
        if latest:
            color = {
                'success': 'green',
                'failed': 'red',
                'running': 'orange',
                'pending': 'gray',
                'aborted': 'darkred'
            }.get(latest.status, 'gray')
            return format_html(
                '<span style="color: {};">#{} - {}</span>',
                color,
                latest.build_number,
                latest.get_status_display()
            )
        return format_html('<span style="color: gray;">No builds</span>')
    latest_build_status.short_description = 'Latest Build'
    
    def success_rate_display(self, obj):
        rate = obj.success_rate
        color = 'green' if rate >= 80 else 'orange' if rate >= 60 else 'red'
        return format_html(
            '<span style="color: {};">{:.1f}%</span>',
            color,
            rate
        )
    success_rate_display.short_description = 'Success Rate'
    
    def latest_build_info(self, obj):
        latest = obj.latest_build
        if latest:
            url = reverse('admin:dashboard_buildrun_change', args=[latest.id])
            return format_html(
                '<a href="{}">Build #{} - {}</a><br>'
                'Started: {}<br>'
                'Duration: {}',
                url,
                latest.build_number,
                latest.get_status_display(),
                latest.started_at.strftime('%Y-%m-%d %H:%M:%S'),
                latest.duration_display
            )
        return 'No builds yet'
    latest_build_info.short_description = 'Latest Build Details'


@admin.register(BuildRun)
class BuildRunAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status', 'author', 'started_at', 'duration_display', 'deployment_count']
    list_filter = ['status', 'job', 'started_at']
    search_fields = ['job__name', 'commit_hash', 'commit_message', 'author']
    readonly_fields = ['started_at', 'duration_display', 'deployment_info']
    
    fieldsets = (
        ('Build Information', {
            'fields': ('job', 'build_number', 'status')
        }),
        ('Git Information', {
            'fields': ('commit_hash', 'commit_message', 'author')
        }),
        ('Timing', {
            'fields': ('started_at', 'finished_at', 'duration')
        }),
        ('Output', {
            'fields': ('log_output',),
            'classes': ('collapse',)
        }),
        ('Deployments', {
            'fields': ('deployment_info',),
            'classes': ('collapse',)
        }),
    )
    
    def deployment_count(self, obj):
        count = obj.deployments.count()
        if count > 0:
            return format_html(
                '<a href="{}?build_run__id__exact={}">{} deployments</a>',
                reverse('admin:dashboard_deployment_changelist'),
                obj.id,
                count
            )
        return '0 deployments'
    deployment_count.short_description = 'Deployments'
    
    def deployment_info(self, obj):
        deployments = obj.deployments.all()
        if deployments:
            info = []
            for deployment in deployments:
                url = reverse('admin:dashboard_deployment_change', args=[deployment.id])
                color = {
                    'success': 'green',
                    'failed': 'red',
                    'deploying': 'orange',
                    'pending': 'gray',
                    'rolled_back': 'darkred'
                }.get(deployment.status, 'gray')
                info.append(format_html(
                    '<a href="{}" style="color: {};">{} - {}</a>',
                    url,
                    color,
                    deployment.environment.name,
                    deployment.get_status_display()
                ))
            return mark_safe('<br>'.join(info))
        return 'No deployments'
    deployment_info.short_description = 'Deployment Details'


@admin.register(Environment)
class EnvironmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'env_type', 'is_active', 'url_link', 'latest_deployment_status', 'created_at']
    list_filter = ['env_type', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'url']
    readonly_fields = ['created_at', 'deployment_history']
    
    fieldsets = (
        ('Environment Information', {
            'fields': ('name', 'env_type', 'description', 'is_active')
        }),
        ('Access', {
            'fields': ('url',)
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
        ('Deployment History', {
            'fields': ('deployment_history',),
            'classes': ('collapse',)
        }),
    )
    
    def url_link(self, obj):
        if obj.url:
            return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
        return '-'
    url_link.short_description = 'URL'
    
    def latest_deployment_status(self, obj):
        latest = obj.deployments.first()
        if latest:
            color = {
                'success': 'green',
                'failed': 'red',
                'deploying': 'orange',
                'pending': 'gray',
                'rolled_back': 'darkred'
            }.get(latest.status, 'gray')
            return format_html(
                '<span style="color: {};">{}</span><br>'
                '<small>{}</small>',
                color,
                latest.get_status_display(),
                latest.deployed_at.strftime('%Y-%m-%d %H:%M')
            )
        return format_html('<span style="color: gray;">No deployments</span>')
    latest_deployment_status.short_description = 'Latest Deployment'
    
    def deployment_history(self, obj):
        deployments = obj.deployments.all()[:10]  # Last 10 deployments
        if deployments:
            history = []
            for deployment in deployments:
                url = reverse('admin:dashboard_deployment_change', args=[deployment.id])
                color = {
                    'success': 'green',
                    'failed': 'red',
                    'deploying': 'orange',
                    'pending': 'gray',
                    'rolled_back': 'darkred'
                }.get(deployment.status, 'gray')
                history.append(format_html(
                    '<a href="{}" style="color: {};">{} - {} ({})</a>',
                    url,
                    color,
                    deployment.build_run,
                    deployment.get_status_display(),
                    deployment.deployed_at.strftime('%Y-%m-%d %H:%M')
                ))
            return mark_safe('<br>'.join(history))
        return 'No deployment history'
    deployment_history.short_description = 'Recent Deployments'


@admin.register(Deployment)
class DeploymentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'status', 'deployed_by', 'deployed_at', 'completed_at']
    list_filter = ['status', 'environment', 'deployed_at']
    search_fields = ['build_run__job__name', 'environment__name', 'deployed_by', 'notes']
    readonly_fields = ['deployed_at']
    
    fieldsets = (
        ('Deployment Information', {
            'fields': ('build_run', 'environment', 'status', 'deployed_by')
        }),
        ('Timing', {
            'fields': ('deployed_at', 'completed_at')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('build_run__job', 'environment')


# Customize admin site
admin.site.site_header = 'Jenkins Dashboard Administration'
admin.site.site_title = 'Jenkins Dashboard Admin'
admin.site.index_title = 'Welcome to Jenkins Dashboard Administration'

