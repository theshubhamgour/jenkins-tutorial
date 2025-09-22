# Python Jenkins Docker Tutorial

This repository contains a **minimal Python application** designed to demonstrate a complete CI/CD workflow using **Jenkins**, **Docker**, and **Docker Compose**.

---

## 📖 Overview

This project is ideal for beginners who want to learn:

- How to create a simple Python application
- How to build and test it using Python's built-in tools
- How to containerize it with Docker
- How to run it with Docker Compose
- How to push a Docker image to Docker Hub via Jenkins

The application itself is a simple **"Hello World"** program with a unit test written using Python's `unittest` framework.

---

## 📂 Project Structure

```
python-jenkins-docker/
│── app.py                  # Main Python Application
│── tests/
│   └── test_app.py         # Unit Tests (unittest)
│── requirements.txt        # Python Dependencies
│── Dockerfile              # Docker Image Definition
│── docker-compose.yml      # Docker Compose Configuration
│── Jenkinsfile             # Jenkins Pipeline Script
│── README.md               # Project Documentation
```

---

## ⚙️ Build, Test, and Run Workflow

### **1️⃣ Build (Local Compilation)**
Python is an interpreted language, so compilation is optional.  
You can check syntax and byte-compile using:
```bash
python -m py_compile app.py
```

---

### **2️⃣ Test**
Run unit tests to verify the application works:
```bash
python -m unittest discover tests
```

---

### **3️⃣ Run Locally**
Run the application directly on your machine:
```bash
python app.py
```
**Expected Output:**
```
Hello from Python Application for Jenkins CI/CD!
```

---

## 🐳 Running with Docker

### **1️⃣ Build Docker image**
```bash
docker build -t python-jenkins-docker:latest .
```

### **2️⃣ Run Docker container**
```bash
docker run --rm python-jenkins-docker:latest
```

**Expected Output:**
```
Hello from Python Application for Jenkins CI/CD!
```

---

## ⚙ Running with Docker Compose

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

The provided `Jenkinsfile` automates the following stages:

1. **Build** – Checks syntax by compiling Python bytecode  
2. **Test** – Runs `unittest` tests  
3. **Docker Build** – Builds a Docker image from the project  
4. **Docker Push** – Pushes the image to Docker Hub

**Jenkinsfile snippet:**
```groovy
pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds') // Jenkins credential ID
        DOCKER_IMAGE = "theshubhamgour/python-jenkins-docker"
    }
    stages {
        stage('Build') {
            steps {
                sh 'python -m py_compile app.py'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }
        stage('Docker Build') {
            steps {
                sh 'docker build -t "$DOCKER_IMAGE:latest" .'
            }
        }
        stage('Docker Push') {
            steps {
                sh 'echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin'
                sh 'docker push "$DOCKER_IMAGE:latest"'
            }
        }
        stage('Docker Run') {
            steps {
                sh 'docker run --rm "$DOCKER_IMAGE:latest"'
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
```

**Note:**  
You must configure a Jenkins credential named `dockerhub-creds` containing your Docker Hub username and password.

---

## 🛠 Prerequisites

Before running this project, install:

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Jenkins](https://www.jenkins.io/) (optional for CI/CD)

---

## 📜 License

This project is released under the MIT License.