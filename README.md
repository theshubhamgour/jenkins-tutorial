# Django CI/CD Demo App

A simple Django web application demonstrating a CI/CD pipeline using Docker and Jenkins. This project showcases a basic UI app with automated build, test, and deployment processes.

## 📖 Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Build the Docker Image](#build-the-docker-image)
  - [Run the Application](#run-the-application)
- [Jenkins CI/CD Pipeline](#jenkins-cicd-pipeline)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 📋 Overview
This project is a minimal Django application designed to demonstrate a CI/CD workflow. It uses Docker for containerization and Jenkins for automating the build, test, and deployment stages. The app serves a basic UI and can be accessed locally after running the Docker container.

## 🛠️ Prerequisites
Before you begin, ensure you have the following installed:
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [Jenkins](https://www.jenkins.io/download/) (optional, for CI/CD pipeline)
- Python 3.8+ (optional, for local development without Docker)

## 🚀 Getting Started

### Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://your-repo-url.git
cd django-cicd-demo
```

### Build the Docker Image
Build the Docker image for the Django application:
```bash
docker build -t django-cicd-demo .
```

### Run the Application
Run the Docker container to start the Django app:
```bash
docker run -d -p 8000:8000 django-cicd-demo
```

Once the container is running, access the application at:
```
http://localhost:8000
```

## 🔄 Jenkins CI/CD Pipeline
This project includes a `Jenkinsfile` that defines a CI/CD pipeline with the following stages:
1. **Clone**: Clones the repository from the specified source.
2. **Build**: Builds the Docker image for the Django app.
3. **Test**: Runs tests (e.g., Django unit tests) to ensure code quality.
4. **Run**: Deploys the Docker container.
5. **Success**: Reports successful pipeline completion.

To set up the Jenkins pipeline:
1. Install and configure Jenkins on your server or local machine.
2. Create a new pipeline job in Jenkins.
3. Point the pipeline to your repository and reference the `Jenkinsfile`.
4. Trigger the pipeline manually or configure webhooks for automatic builds.

Example `Jenkinsfile` snippet:
```groovy
pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://your-repo-url.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t django-cicd-demo .'
            }
        }
        stage('Test') {
            steps {
                sh 'docker run django-cicd-demo python manage.py test'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8000:8000 django-cicd-demo'
            }
        }
        stage('Success') {
            steps {
                echo 'Pipeline completed successfully!'
            }
        }
    }
}
```

## 📂 Project Structure
```
django-cicd-demo/
├── Dockerfile          # Docker configuration for building the image
├── Jenkinsfile         # Jenkins pipeline configuration
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── app/                # Django app directory
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── views.py        # Django views
│   └── ...
├── README.md           # Project documentation
└── ...
```

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes tests.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy coding! 🚀