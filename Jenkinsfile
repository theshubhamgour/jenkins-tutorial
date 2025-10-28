pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DockerPass', usernameVariable: 'DockerUser')]) {
                    echo "Hello World"
                    echo "Docker username: ${DockerUser}"
                    // You can use the credentials here, for example:
                    // sh "docker login -u ${DockerUser} -p ${DockerPass}"
                }
            }
        }
    }
}