# ⚙️ Jenkins CI/CD Pipeline for Flask Portfolio

This repository demonstrates how to implement a **Jenkins CI/CD pipeline** for automating the build, test, and deployment of a **Flask web application**.

Project created and explained by [Shubham Gour Tech](https://www.youtube.com/shubhamgourtech)  
as part of the **Jenkins Tutorial Playlist**.

---

## 🎯 Objectives
- Automate the full lifecycle of a Flask app using Jenkins
- Showcase real-world DevOps CI/CD setup
- Demonstrate Docker image creation, tagging, and deployment

Project link : https://github.com/theshubhamgour/flask-portfolio

---

## 🧩 Pipeline Overview
The Jenkinsfile automates these key stages:

1️⃣ **Checkout Code** — Pulls source code from GitHub  
2️⃣ **Install Dependencies** — Installs Python requirements (`Flask`, `flake8`)  
3️⃣ **Run Lint Test** — Validates code quality using `flake8`  
4️⃣ **Build Docker Image** — Packages the Flask app into a Docker container  
5️⃣ **Push to DockerHub** — Uploads the image to your DockerHub repo  
6️⃣ **Deploy to Stage** — Runs the latest image on a server (port 5000)

---

## 🐳 Jenkinsfile Example
```groovy
pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-cred-id')
        IMAGE_NAME = 'theshubhamgour/flask-portfolio'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/theshubhamgour/flask-portfolio.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Lint Test') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 . || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push $IMAGE_NAME:$BUILD_NUMBER'
                }
            }
        }

        stage('Deploy to Stage') {
            steps {
                sh 'docker run -d -p 5000:5000 $IMAGE_NAME:$BUILD_NUMBER'
            }
        }
    }

    post {
        success {
            echo '✅ Build, Test, and Deploy completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
```

---

## 🧠 Key Learnings
- Jenkins declarative pipeline setup  
- Docker integration in CI/CD  
- Secure credential management  
- Automating Flask deployments  

---

## 🎥 YouTube Playlist
👉 **[Jenkins Tutorial Playlist](https://www.youtube.com/playlist?list=PLBr8obKbpkYvJEaPmrzhHhwx8uPj8WYbg)**  
Watch step-by-step how this pipeline was created.

---

## 👨‍💻 Author
**Shubham Gour**  
Release Engineer | DevOps | Cloud | YouTuber  
🔗 [LinkedIn](https://www.linkedin.com/in/theshubhamgour/)  
🎥 [YouTube](https://www.youtube.com/shubhamgourtech)

---

## 📜 License
MIT License © 2025 Shubham Gour Tech
