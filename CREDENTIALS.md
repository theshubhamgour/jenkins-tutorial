# Jenkins Dashboard - Demo Credentials

## 🔐 Admin Access Credentials

For demo and tutorial purposes, the application automatically creates a hardcoded admin user during the data population process.

### Default Admin User
- **Username**: `admin`
- **Email**: `admin@example.com`
- **Password**: `admin123`

### Access URLs
- **Local Development**: http://localhost:8000/admin/
- **Docker Deployment**: http://localhost/admin/

## 🚀 Automatic User Creation

The admin user is automatically created when running:
```bash
python manage.py populate_sample_data
```

This command is executed automatically in both Docker configurations:
- `docker-compose.yml` (Production)
- `docker-compose.dev.yml` (Development)

## 🎯 Demo Purpose

These hardcoded credentials are specifically designed for:
- **YouTube Tutorials**: No interactive setup required
- **Demo Environments**: Consistent access across deployments
- **CI/CD Pipelines**: Prevents pipeline failures from user input prompts
- **Educational Content**: Focus on application features, not setup

## ⚠️ Security Note

**Important**: These are demo credentials only. For production use:
1. Change the default password immediately
2. Use environment variables for credentials
3. Implement proper user management
4. Enable two-factor authentication if needed

## 🔄 Resetting Credentials

To reset or recreate the admin user:
```bash
# Clear all data and recreate (including admin user)
python manage.py populate_sample_data --clear

# Or manually in Django shell
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.filter(username='admin').delete()
>>> User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
```

## 📋 Additional Demo Users

The application currently creates only one admin user. To add more demo users for tutorials, you can modify the `create_superuser` method in:
`dashboard/management/commands/populate_sample_data.py`

Example additional users:
- **Developer**: `dev` / `dev123`
- **Manager**: `manager` / `manager123`
- **Viewer**: `viewer` / `viewer123` (staff, no superuser)

