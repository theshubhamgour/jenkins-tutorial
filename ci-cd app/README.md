# Jenkins Docker CI/CD Pipeline

A production-style Jenkins CI/CD pipeline for Node.js applications.

## Features

- Source Code Checkout
- Automated Testing
- Docker Build
- Docker Hub Push
- SSH Deployment
- Health Check Validation
- Slack Notifications

## Required Jenkins Credentials

| Credential ID | Type |
|--------------|------|
| dockerhub-username | Secret Text |
| dockerhub-creds | Username + Password |
| server-ip | Secret Text |
| server-ssh-key | SSH Private Key |
| slack-webhook-url | Secret Text |

## Pipeline Flow

GitHub Push
↓
Checkout
↓
Test
↓
Docker Build
↓
Docker Hub Push
↓
Deploy
↓
Health Check
↓
Slack Notification