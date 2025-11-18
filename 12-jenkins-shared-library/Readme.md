# Jenkins Shared Library - Documentation

This repository contains reusable Jenkins Shared Library functions to simplify CI/CD pipelines.

## Files Included

### 1. **hello.groovy**
A basic function printing a standard Hello World.

```groovy
def call(){
    echo "Hello, World!"
}
```

### 2. **hello2.groovy**
Prints a personalized welcome message.

```groovy
def call(String name = "User") {
    echo "Hello, ${name}! Welcome to Jenkins Shared Library."
}
```

### 3. **customLog.groovy**
Adds a formatted log section around any message.

```groovy
def call(String msg) {
    echo "===================="
    echo "   ${msg}"
    echo "===================="
}
```

### 4. **dockerBuildPush.groovy**
Reusable Docker Build & Push stage using stored credentials.

```groovy
def call(String imageName) {
    stage('Docker Build & Push') {
        withCredentials([usernamePassword(credentialsId: 'DockerHub',
                                           usernameVariable: 'USER',
                                           passwordVariable: 'PASS')]) {
            sh '''
               echo "$PASS" | docker login -u "$USER" --password-stdin
               docker build -t ${imageName} .
               docker push ${imageName}
            '''
        }
    }
}
```

## How to Use These in Jenkinsfile

```groovy
@Library('my-shared-lib') _

pipeline {
    agent any

    stages {
        stage('Example') {
            steps {
                hello()
                hello2("Shubham")
                customLog("Starting Build")
                dockerBuildPush("theshubhamgour/demo-app:latest")
            }
        }
    }
}
```

## Notes
- Configure your Shared Library under: Manage Jenkins → Configure System → Global Pipeline Libraries
- Ensure your credentials ID matches the scripts.
