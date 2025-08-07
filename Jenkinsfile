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
                sh 'docker run --rm django-cicd-demo python manage.py check'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8000:8000 --name django-app django-cicd-demo'
            }
        }

        stage('Success') {
            steps {
                echo 'CI/CD pipeline completed successfully.'
            }
        }
    }
}
