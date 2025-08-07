from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
import random
from dashboard.models import BuildJob, BuildRun, Environment, Deployment


class Command(BaseCommand):
    help = 'Populate the database with sample data for Jenkins tutorial'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            Deployment.objects.all().delete()
            BuildRun.objects.all().delete()
            BuildJob.objects.all().delete()
            Environment.objects.all().delete()

        self.stdout.write('Creating admin superuser...')
        self.create_superuser()

        self.stdout.write('Creating sample environments...')
        self.create_environments()

        self.stdout.write('Creating sample build jobs...')
        self.create_build_jobs()

        self.stdout.write('Creating sample build runs...')
        self.create_build_runs()

        self.stdout.write('Creating sample deployments...')
        self.create_deployments()

        self.stdout.write(
            self.style.SUCCESS('Successfully populated database with sample data!')
        )

    def create_superuser(self):
        """Create a hardcoded superuser for demo purposes"""
        username = 'admin'
        email = 'admin@example.com'
        password = 'admin123'
        
        # Check if superuser already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superuser "{username}" already exists, skipping creation.')
            return
        
        # Create the superuser
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        self.stdout.write(f'Created superuser: {username} (password: {password})')

    def create_environments(self):
        environments = [
            {
                'name': 'Development',
                'env_type': 'development',
                'url': 'https://dev.example.com',
                'description': 'Development environment for testing new features'
            },
            {
                'name': 'Staging',
                'env_type': 'staging',
                'url': 'https://staging.example.com',
                'description': 'Staging environment for pre-production testing'
            },
            {
                'name': 'Production',
                'env_type': 'production',
                'url': 'https://example.com',
                'description': 'Production environment serving live traffic'
            },
            {
                'name': 'QA Testing',
                'env_type': 'testing',
                'url': 'https://qa.example.com',
                'description': 'Quality assurance testing environment'
            }
        ]

        for env_data in environments:
            Environment.objects.get_or_create(
                name=env_data['name'],
                defaults=env_data
            )

    def create_build_jobs(self):
        jobs = [
            {
                'name': 'web-frontend',
                'description': 'React frontend application build and test pipeline',
                'repository_url': 'https://github.com/company/web-frontend.git',
                'branch': 'main',
                'status': 'active'
            },
            {
                'name': 'api-backend',
                'description': 'Django REST API backend service',
                'repository_url': 'https://github.com/company/api-backend.git',
                'branch': 'main',
                'status': 'active'
            },
            {
                'name': 'mobile-app',
                'description': 'React Native mobile application',
                'repository_url': 'https://github.com/company/mobile-app.git',
                'branch': 'develop',
                'status': 'active'
            },
            {
                'name': 'data-pipeline',
                'description': 'ETL data processing pipeline',
                'repository_url': 'https://github.com/company/data-pipeline.git',
                'branch': 'main',
                'status': 'active'
            },
            {
                'name': 'legacy-system',
                'description': 'Legacy Java application (deprecated)',
                'repository_url': 'https://github.com/company/legacy-system.git',
                'branch': 'master',
                'status': 'disabled'
            }
        ]

        for job_data in jobs:
            BuildJob.objects.get_or_create(
                name=job_data['name'],
                defaults=job_data
            )

    def create_build_runs(self):
        jobs = BuildJob.objects.all()
        statuses = ['success', 'failed', 'running', 'pending', 'aborted']
        authors = ['john.doe', 'jane.smith', 'bob.wilson', 'alice.johnson', 'mike.brown']
        
        commit_messages = [
            'Fix authentication bug in login flow',
            'Add new user dashboard feature',
            'Update dependencies to latest versions',
            'Implement API rate limiting',
            'Fix responsive design issues',
            'Add unit tests for user service',
            'Optimize database queries',
            'Update documentation',
            'Fix memory leak in background tasks',
            'Add error handling for edge cases'
        ]

        for job in jobs:
            # Create builds for the last 30 days
            for i in range(random.randint(10, 30)):
                build_number = i + 1
                started_at = timezone.now() - timedelta(
                    days=random.randint(0, 30),
                    hours=random.randint(0, 23),
                    minutes=random.randint(0, 59)
                )
                
                # Most recent builds are more likely to be successful
                if i < 5:  # Recent builds
                    status = random.choices(
                        statuses,
                        weights=[70, 15, 10, 3, 2],  # Higher success rate for recent builds
                        k=1
                    )[0]
                else:  # Older builds
                    status = random.choices(
                        statuses,
                        weights=[60, 25, 5, 5, 5],
                        k=1
                    )[0]

                finished_at = None
                duration = None
                
                if status not in ['running', 'pending']:
                    duration_minutes = random.randint(2, 45)
                    duration = timedelta(minutes=duration_minutes)
                    finished_at = started_at + duration

                # Generate realistic log output
                log_output = self.generate_log_output(job.name, status)

                BuildRun.objects.get_or_create(
                    job=job,
                    build_number=build_number,
                    defaults={
                        'status': status,
                        'commit_hash': f'a{random.randint(100000, 999999)}b{random.randint(100000, 999999)}',
                        'commit_message': random.choice(commit_messages),
                        'author': random.choice(authors),
                        'started_at': started_at,
                        'finished_at': finished_at,
                        'duration': duration,
                        'log_output': log_output
                    }
                )

    def generate_log_output(self, job_name, status):
        """Generate realistic build log output"""
        logs = [
            f"Started by user jenkins",
            f"Building in workspace /var/jenkins_home/workspace/{job_name}",
            f"Cloning the remote Git repository",
            f"Checking out Revision a{random.randint(100000, 999999)}b{random.randint(100000, 999999)}",
            f"[{job_name}] $ /bin/sh -xe /tmp/jenkins{random.randint(1000000000, 9999999999)}.sh",
            f"+ echo 'Starting build process...'",
            f"Starting build process...",
            f"+ npm install",
            f"npm WARN deprecated package@1.0.0: This package is deprecated",
            f"added 1247 packages from 837 contributors and audited 1247 packages in 23.456s",
            f"+ npm run build",
            f"Creating an optimized production build...",
            f"Compiled successfully in 45.67s",
            f"+ npm test",
            f"PASS src/components/Header.test.js",
            f"PASS src/utils/helpers.test.js",
            f"Test Suites: 12 passed, 12 total",
            f"Tests: 89 passed, 89 total",
            f"Snapshots: 0 total",
            f"Time: 12.345s"
        ]

        if status == 'failed':
            logs.extend([
                f"FAIL src/components/Login.test.js",
                f"  ● Login component › should handle invalid credentials",
                f"    expect(received).toBe(expected) // Object.is equality",
                f"    Expected: true",
                f"    Received: false",
                f"Test Suites: 1 failed, 11 passed, 12 total",
                f"Tests: 1 failed, 88 passed, 89 total",
                f"Build step 'Execute shell' marked build as failure",
                f"Finished: FAILURE"
            ])
        elif status == 'success':
            logs.extend([
                f"+ docker build -t {job_name}:latest .",
                f"Successfully built docker image",
                f"+ docker push registry.example.com/{job_name}:latest",
                f"The push refers to repository [registry.example.com/{job_name}]",
                f"latest: digest: sha256:a{random.randint(10000000, 99999999)} size: 1234",
                f"Archiving artifacts",
                f"Finished: SUCCESS"
            ])
        elif status == 'running':
            logs.extend([
                f"Running tests...",
                f"Test progress: 67% complete"
            ])

        return '\n'.join(logs)

    def create_deployments(self):
        environments = Environment.objects.all()
        build_runs = BuildRun.objects.filter(status='success')
        
        deployment_statuses = ['success', 'failed', 'deploying', 'pending', 'rolled_back']
        deployers = ['jenkins-auto', 'john.doe', 'jane.smith', 'ops-team']

        # Create deployments for successful builds
        for build_run in build_runs[:20]:  # Only deploy some builds
            # Randomly deploy to 1-3 environments
            selected_envs = random.sample(list(environments), random.randint(1, 3))
            
            for env in selected_envs:
                # Skip some combinations to make it more realistic
                if random.random() < 0.3:
                    continue
                    
                deployed_at = build_run.finished_at + timedelta(minutes=random.randint(5, 60))
                
                status = random.choices(
                    deployment_statuses,
                    weights=[70, 15, 5, 5, 5],
                    k=1
                )[0]
                
                completed_at = None
                if status not in ['deploying', 'pending']:
                    completed_at = deployed_at + timedelta(minutes=random.randint(2, 15))

                notes = ''
                if status == 'failed':
                    notes = 'Deployment failed due to database migration issues'
                elif status == 'rolled_back':
                    notes = 'Rolled back due to performance issues in production'

                Deployment.objects.get_or_create(
                    build_run=build_run,
                    environment=env,
                    defaults={
                        'status': status,
                        'deployed_by': random.choice(deployers),
                        'deployed_at': deployed_at,
                        'completed_at': completed_at,
                        'notes': notes
                    }
                )

