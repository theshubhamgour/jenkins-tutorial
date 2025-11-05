# 🧩 Jenkins Tutorial – CI/CD Pipeline for GitHub Profile Summarizer

This README explains the **complete Jenkins CI/CD pipeline** you built for the **GitHub Profile Summarizer** project — a React + Vite + Tailwind web application that summarizes GitHub profiles with a clean and interactive UI.

---

## 🎯 Objective

In this Jenkins tutorial, you’ll learn how to:

* Automate the build and deployment process of a React app
* Use Jenkins to build and push Docker images
* Automatically deploy the containerized app after each successful build

---

## 🧱 Application Overview

Github repo (Project Link) : https://github.com/theshubhamgour/github-profile-summarizer.git

**GitHub Profile Summarizer** is a web app that allows users to:

* Enter any GitHub username
* Fetch profile details, repositories, and programming languages
* Visualize data via charts
* Deploy and serve it using Nginx (via Docker container)

Tech Stack:

* ⚛️ React + Vite + Tailwind
* 🧩 Recharts for visualization
* 🐳 Docker + Nginx
* ⚙️ Jenkins for CI/CD

---

## ⚙️ Jenkinsfile (Pipeline Script)

Below is the final pipeline you implemented:

```groovy
pipeline {
  agent any

  environment {
    IMAGE_NAME = "theshubhamgour/github-profile-summarizer"
    IMAGE_TAG = "v${env.BUILD_NUMBER}"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build (Node)') {
      steps {
        sh 'npm install'
        sh 'npm run build'
      }
    }

    stage('Docker Build') {
      steps {
        sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
      }
    }

    stage('Docker Login & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
        }
        sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
        sh 'docker tag $IMAGE_NAME:$IMAGE_TAG $IMAGE_NAME:latest'
        sh 'docker push $IMAGE_NAME:latest'
      }
    }

    stage('Deploy image') {
      steps {
        sh 'docker run -d -p 8081:80 $IMAGE_NAME:$IMAGE_TAG'
      }
    }
  }

  post {
    always {
      echo "✅ Image pushed: $IMAGE_NAME:$IMAGE_TAG"
    }
  }
}
```

---

## 🔍 Pipeline Breakdown

### 🪣 1. **Checkout**

* Pulls the latest code from your GitHub repository using `checkout scm`.
* Ensures that every build runs on the latest commit.

### ⚙️ 2. **Build (Node)**

* Runs inside Jenkins agent.
* Installs dependencies using `npm install`.
* Builds the production files using `npm run build` (generates `/dist`).

### 🐳 3. **Docker Build**

* Builds a Docker image using the provided **Dockerfile**:

  * Stage 1: Builds the app in Node environment
  * Stage 2: Serves the compiled app using Nginx
* Tags the image as `theshubhamgour/github-profile-summarizer:v<build_number>`

### 🔐 4. **Docker Login & Push**

* Logs into DockerHub using Jenkins credentials (`DockerHub`).
* Pushes both versioned and `latest` tags to your DockerHub repo.

### 🚀 5. **Deploy Image**

* Automatically runs the container on the Jenkins host using the new image.
* Maps container port **80** to host port **8081**:

  * App becomes accessible at → **http://<jenkins-server-ip>:8081**

### ✅ Post Section

* Displays confirmation that the image was built and pushed successfully.

---

## 🧩 Dockerfile (Used in Pipeline)

```dockerfile
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## 📦 Jenkins Credentials Setup

In Jenkins:

1. Go to **Manage Jenkins → Credentials → Global → Add Credentials**
2. Choose **Username and Password** type
3. ID: `DockerHub`
4. Username: your DockerHub username
5. Password: your DockerHub password

---

## 🧠 Flow Summary

| Step | Action                            | Output                    |
| ---- | --------------------------------- | ------------------------- |
| 1️⃣  | Jenkins pulls latest GitHub code  | Source code ready         |
| 2️⃣  | Jenkins builds React app          | Compiled files in `/dist` |
| 3️⃣  | Jenkins builds Docker image       | Container image created   |
| 4️⃣  | Jenkins pushes image to DockerHub | Versioned + latest tags   |
| 5️⃣  | Jenkins deploys container         | Live app on port 8081     |

---

## 💡 Tips for YouTube Explanation

* Highlight **multi-stage Docker build** (small, optimized image).
* Show Jenkins credentials integration visually.
* Demonstrate how Jenkins automatically deploys the app after every commit.
* End the video by opening **[http://localhost:8081](http://localhost:8081)** to show live deployment.

---

## 🧠 Next Steps

* Add automatic **container cleanup** before deploying new builds.
* Integrate **Slack notifications** for build success/failure.
* Deploy to **AWS EC2 or Kubernetes** using Jenkins pipelines.

---

## 📄 License

MIT © 2025 Shubham Gour
Created for Jenkins CI/CD YouTube tutorial demonstration.
