pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t java-jenkins-docker:latest .'
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker run --rm java-jenkins-docker:latest'
            }
        }        
    }
}
