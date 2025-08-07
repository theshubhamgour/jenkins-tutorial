from django.db import models
from django.utils import timezone


class BuildJob(models.Model):
    """Model representing a Jenkins build job/pipeline"""
    
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('disabled', 'Disabled'),
        ('archived', 'Archived'),
    ]
    
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    repository_url = models.URLField(blank=True)
    branch = models.CharField(max_length=100, default='main')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-updated_at']
    
    def __str__(self):
        return self.name
    
    @property
    def latest_build(self):
        """Get the most recent build run for this job"""
        return self.build_runs.first()
    
    @property
    def success_rate(self):
        """Calculate success rate of recent builds"""
        recent_builds = self.build_runs.all()[:10]
        if not recent_builds:
            return 0
        successful = sum(1 for build in recent_builds if build.status == 'success')
        return (successful / len(recent_builds)) * 100


class BuildRun(models.Model):
    """Model representing a single build execution"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('running', 'Running'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('aborted', 'Aborted'),
    ]
    
    job = models.ForeignKey(BuildJob, on_delete=models.CASCADE, related_name='build_runs')
    build_number = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    commit_hash = models.CharField(max_length=40, blank=True)
    commit_message = models.TextField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    started_at = models.DateTimeField(default=timezone.now)
    finished_at = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    log_output = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-build_number']
        unique_together = ['job', 'build_number']
    
    def __str__(self):
        return f"{self.job.name} #{self.build_number}"
    
    @property
    def is_running(self):
        return self.status in ['pending', 'running']
    
    @property
    def duration_display(self):
        """Display duration in a human-readable format"""
        if not self.duration:
            return "N/A"
        total_seconds = int(self.duration.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        if minutes > 0:
            return f"{minutes}m {seconds}s"
        return f"{seconds}s"


class Environment(models.Model):
    """Model representing deployment environments"""
    
    ENV_TYPES = [
        ('development', 'Development'),
        ('staging', 'Staging'),
        ('production', 'Production'),
        ('testing', 'Testing'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    env_type = models.CharField(max_length=20, choices=ENV_TYPES)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['env_type', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.get_env_type_display()})"


class Deployment(models.Model):
    """Model representing a deployment to an environment"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('deploying', 'Deploying'),
        ('success', 'Success'),
        ('failed', 'Failed'),
        ('rolled_back', 'Rolled Back'),
    ]
    
    build_run = models.ForeignKey(BuildRun, on_delete=models.CASCADE, related_name='deployments')
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='deployments')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    deployed_by = models.CharField(max_length=100, blank=True)
    deployed_at = models.DateTimeField(default=timezone.now)
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-deployed_at']
        unique_together = ['build_run', 'environment']
    
    def __str__(self):
        return f"{self.build_run} → {self.environment.name}"

