# Jenkins Installation Guide

This guide provides step-by-step instructions to install Jenkins on a Debian-based system.

## Pre-Requisites

- **Java (JDK)**: Jenkins requires Java to run. We recommend using OpenJDK 17.

## Installation Steps

### 1. Install Java

Update the package index and install OpenJDK 17 JRE:

```bash
sudo apt update
sudo apt install openjdk-17-jre
```

Verify Java installation:

```bash
java -version
```

### 2. Install Jenkins (Long-Term Support Release)

Jenkins provides a Long-Term Support (LTS) release every 12 weeks, chosen from the stream of regular releases for stability. Follow these steps to install Jenkins from the Debian-stable apt repository:

```bash
sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

## Next Steps

- Once installed, Jenkins can be accessed via `http://localhost:8080` in your web browser.
- Follow the on-screen instructions to complete the initial setup, including retrieving the initial admin password and installing suggested plugins.
