# Java Jenkins Docker Tutorial

This repository contains a **minimal Java application** designed to demonstrate a complete CI/CD workflow using **Jenkins**, **Maven**, **Docker**, and **Docker Compose**.

---

## 📖 Overview

<img width="1459" height="281" alt="image" src="https://github.com/user-attachments/assets/369bb6bc-bdf9-4808-b1a1-bbca9ba0be5e" />

This project is intended for beginners who want to learn:

- How to create a simple Java application
- How to build, compile, and test it using **Maven**
- How to containerize it with **Docker**
- How to run it using **Docker Compose**
- How to automate the entire workflow using a **Jenkins pipeline**

The application itself is a simple Java "Hello World" program with a basic **JUnit** test.

---

## 📂 Project Structure

```
java-jenkins-docker/
│── src/
│   ├── main/java/com/example/App.java         # Main Java Application
│   └── test/java/com/example/AppTest.java     # Unit Tests (JUnit)
│── pom.xml                                    # Maven Build File
│── Dockerfile                                 # Docker Image Definition
│── docker-compose.yml                         # Docker Compose Configuration
│── Jenkinsfile                                # Jenkins Pipeline Script
│── README.md                                  # Project Documentation
```

---

## ⚙️ Build, Test, and Compile Workflow

### **1️⃣ Build**
We use Maven to compile the Java source code:
```bash
mvn clean package
```
- **`mvn clean`** removes any previous build artifacts.
- **`mvn package`** compiles the code and packages it into a JAR file.
- Output JAR: `target/java-jenkins-docker-1.0-SNAPSHOT.jar`

---

### **2️⃣ Test**
The project includes a basic **JUnit test**:
```bash
mvn test
```
This runs all tests inside the `src/test/java` directory.

---

### **3️⃣ Compile**
Maven automatically compiles the Java source files during the `package` phase:
```bash
mvn compile
```
This ensures all Java files are translated into `.class` files in the `target/classes` directory.

---

## 🚀 Running Locally

After building the project, run the application locally:

```bash
java -jar target/java-jenkins-docker-1.0-SNAPSHOT.jar
```

**Expected Output:**
```
Hello from Java Application for Jenkins CI/CD!
```

---

## 🐳 Running with Docker

### **1️⃣ Build Docker image**
```bash
docker build -t java-jenkins-docker:latest .
```

### **2️⃣ Run Docker container**
```bash
docker run --rm java-jenkins-docker:latest
```

---

## ⚙ Running with Docker Compose

If you want to run the app using Docker Compose:

### **1️⃣ Build & run services**
```bash
docker-compose up --build
```

### **2️⃣ Stop services**
```bash
docker-compose down
```

---

## 🔄 Jenkins Pipeline

The provided `Jenkinsfile` automates the process:

```groovy
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

```
## 🌟 Advanced End-to-End CI/CD Pipeline

For a complete, production-ready deployment workflow, you can use the following advanced pipeline. This includes automated Git checkout, directory management, Docker registry tagging, secure credential management for pushing to Docker Hub, and automated workspace cleanup.

```groovy
pipeline {
    agent any
    
    // Define variables to make the pipeline reusable and easier to read
    environment {
        IMAGE_NAME = 'java-jenkins-docker'
        DOCKER_HUB_USER = 'your_dockerhub_username' // Replace with your actual Docker Hub username
        DOCKER_CREDS_ID = 'docker-hub-credentials'  // The ID of the credentials stored in Jenkins
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/theshubhamgour/jenkins-tutorial.git'
            }
        }
        stage('Build') {
            steps {
                dir('3-java-jenkins-docker-app') {
                    sh 'mvn clean package'
                }
            }
        }
        stage('Test') {
            steps {
                dir('3-java-jenkins-docker-app') {
                    sh 'mvn test'
                }
            }
        }
        stage('Docker Build') {
            steps {
                dir('3-java-jenkins-docker-app') {
                    // Build the initial local image
                    sh "docker build -t ${IMAGE_NAME}:latest ."
                }
            }
        }
        stage('Docker Tag') {
            steps {
                // Tag the image with your Docker registry username so it can be pushed
                sh "docker tag ${IMAGE_NAME}:latest ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
            }
        }
        stage('Docker Login & Push') {
            steps {
                // Securely fetch credentials from Jenkins to login
                withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDS_ID}", passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    // Use --password-stdin to prevent the password from showing up in Jenkins logs
                    sh "echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin"
                    
                    // Push the tagged image to the registry
                    sh "docker push ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest"
                }
            }
        }        
    }
    
    // The post block runs after all stages are complete
    post {
        always {
            // Cleans the Jenkins workspace directory 
            cleanWs()
            
            // Optional: Remove the local Docker images to free up space on the Jenkins server
            sh "docker rmi ${IMAGE_NAME}:latest || true"
            sh "docker rmi ${DOCKER_HUB_USER}/${IMAGE_NAME}:latest || true"
        }
    }
}
```

![Jenkins Pipeline Success](https://i.ibb.co/Hfh3FJHF/Screenshot-2026-04-15-192141.png)

**Pipeline Stages:**
1. **Build** – Compiles and packages the Java code
2. **Test** – Runs JUnit tests
3. **Docker Build & Run** – Builds and runs the Docker image

---

## 🛠 Prerequisites

You need to have the following installed:

- [Java 17+](https://adoptium.net/)
- [Apache Maven](https://maven.apache.org/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Jenkins](https://www.jenkins.io/) (optional for CI/CD testing)

---

## 📜 License

This project is released under the MIT License.
