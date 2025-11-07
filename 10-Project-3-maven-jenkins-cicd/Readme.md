# 🧩 Maven Jenkins CI/CD Project Summary

This repository demonstrates a **complete CI/CD pipeline** using **Jenkins**, **Maven**, and **Docker**, created for educational purposes on Shubham Gour’s YouTube channel.

📦 **Project Repository:**  
👉 [https://github.com/theshubhamgour/maven-jenkins-cicd-demo](https://github.com/theshubhamgour/maven-jenkins-cicd-demo)

---

## 🚀 What This Project Covers

- **Build Automation:** Maven used to compile and package a Java application  
- **Unit Testing:** JUnit for automated testing integrated within Jenkins  
- **Dockerization:** Application is containerized with Docker  
- **Image Deployment:** Jenkins pushes the Docker image to DockerHub  
- **Pipeline Automation:** A multi-stage Jenkinsfile handles everything — from build to deploy  

---

## ⚙️ Jenkins Pipeline Stages

1. 🧹 **Clean Workspace** — Remove old files  
2. 🏗️ **Build** — Compile Java code  
3. 🧪 **Test** — Run JUnit tests and publish results  
4. 📦 **Package** — Create executable JAR  
5. 🔍 **Static Code Analysis** — Quality check (optional)  
6. 🐳 **Docker Build** — Build Docker image  
7. 🔐 **Login to DockerHub**  
8. 🚀 **Push Image** — Upload image to DockerHub  
9. ⚙️ **Deploy Container** — Run the built container  
10. 🧾 **Post-Deployment Check** — Validate the app  
11. 🧼 **Cleanup** — Stop and remove containers/images  

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|----------|
| **Java 17** | Core application |
| **Maven** | Build automation |
| **JUnit 4** | Testing framework |
| **Docker** | Containerization |
| **Jenkins** | CI/CD automation |
| **GitHub** | SCM integration |

---

## 📂 Key Files

| File | Description |
|------|-------------|
| `pom.xml` | Maven project configuration |
| `Dockerfile` | Docker build instructions |
| `Jenkinsfile` | CI/CD pipeline definition |
| `Application.java` | Java source file |
| `ApplicationTests.java` | Unit tests |

---

## 🎥 Tutorial Reference

Watch the full step-by-step tutorial on YouTube:  
👉 [#theshubhamgour](https://www.youtube.com/@theshubhamgour)

---

## 🧾 Author

**Created by:** [Shubham Gour](https://github.com/theshubhamgour)  
**Project Link:** [https://github.com/theshubhamgour/maven-jenkins-cicd-demo](https://github.com/theshubhamgour/maven-jenkins-cicd-demo)

> 💡 Follow for more DevOps tutorials and hands-on CI/CD projects.
