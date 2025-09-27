pipeline {
    agent any
    stages {
        stage('Clone Github Repository') {
            steps {
                git branch: 'main', changelog: false, poll: false, url: 'https://github.com/theshubhamgour/jenkins-tutorial.git'
                sh 'pwd'
            }
        }        
        stage('Build') {
            steps {
                dir('4-python-jenkins-docker-app') {
                    sh 'python3 -m py_compile app.py'
                }
            }
        }
        stage('Test') {
            steps {
                dir('4-python-jenkins-docker-app') {
                    sh 'python3 -m unittest discover tests'
                }
            }
        }
        stage('Docker Build') {
            steps {
                dir('4-python-jenkins-docker-app') {
                    sh 'docker build -t python-app:latest .'
                }
            }
        }
        stage('Docker Run') {
            steps {
                dir('4-python-jenkins-docker-app') {
                    sh 'docker run --rm python-app:latest'
                }
            }
        } 
        stage('Docker Tag & Push') {
            steps {
                dir('4-python-jenkins-docker-app') {
                    withCredentials([usernamePassword(credentialsId: 'theshubhamgour',
                                                      passwordVariable: 'DockerhubPassword',
                                                      usernameVariable: 'DockerhubUserName')]) {
                        sh '''
                            echo "$DockerhubPassword" | docker login -u "$DockerhubUserName" --password-stdin
                            docker tag python-app:latest theshubhamgour/python-app:latest
                            docker push theshubhamgour/python-app:latest
                        '''
                    }
                }
            }
        }         
    }
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
