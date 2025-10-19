# 🌱 Understanding Environment Variables in Jenkins

Environment variables in Jenkins are key-value pairs that store information and configuration data.  
They make your Jenkins pipelines **flexible**, **secure**, and **reusable** by avoiding hardcoded values like credentials, paths, or application names.

---

## 🔍 What Are Environment Variables?

Environment variables are values that can be used throughout your Jenkins job or pipeline.  
They allow Jenkins to dynamically use settings like:

- The build number  
- Job name  
- Git branch name  
- DockerHub credentials  
- Environment type (DEV/QA/PROD)

Example:

```
echo "Running build number: $BUILD_NUMBER"
```

Here, `$BUILD_NUMBER` is a **built-in Jenkins environment variable**.

---

## ⚙️ Types of Environment Variables in Jenkins

### 1. Built-in Variables

These are automatically provided by Jenkins for every job.

| Variable      | Example Value                          | Description                        |
|----------------|----------------------------------------|------------------------------------|
| BUILD_NUMBER   | 25                                     | Unique number for each build       |
| JOB_NAME       | python-app-build                       | Name of the current Jenkins job    |
| WORKSPACE      | /var/lib/jenkins/workspace/python-app  | Path to the current job’s workspace |
| GIT_COMMIT     | ab12cd34                               | Current Git commit hash            |

You can print them in a shell step:

```
echo "Build #$BUILD_NUMBER running in $WORKSPACE"
```

---

### 2. Global Environment Variables

Configured once and available to **all jobs** in Jenkins.

**Steps to configure:**
1. Go to **Manage Jenkins → Configure System**  
2. Scroll to **Global properties → Environment variables**  
3. Add key-value pairs (e.g., `ENV_TYPE=QA`)

Usage in shell:

```
echo "Deploying to $ENV_TYPE environment"
```

---

### 3. Job-Specific Variables

Set directly in a particular Jenkins job configuration.

**Steps:**
1. Open your Jenkins job → **Configure**
2. Under **Build Environment**, check **“Inject environment variables”**
3. Add key-value pairs (e.g., `APP_VERSION=1.0.0`)

Usage:

```
echo "Building version $APP_VERSION"
```

---

### 4. Pipeline Environment Variables

Defined inside the **Jenkinsfile** using the `environment {}` block.

Example:

```
pipeline {
    agent any
    environment {
        APP_NAME = 'my-python-app'
        DEPLOY_ENV = 'DEV'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building ${APP_NAME} for ${DEPLOY_ENV}"
            }
        }
    }
}
```

---

### 5. Credential-Based Environment Variables

Used for **secure data** like passwords, tokens, or Docker credentials.  
Jenkins stores them securely in its **Credentials Manager** and injects them safely at runtime.

Example:

```
withCredentials([usernamePassword(credentialsId: 'Dockerhub-Cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
    sh '''
        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
    '''
}
```

---

## 🔒 Why Use Environment Variables?

✅ Avoid hardcoding secrets or configurations  
✅ Reuse pipelines across multiple environments  
✅ Keep builds portable and maintainable  
✅ Simplify CI/CD configuration management  

---

## 🧠 Pro Tips

- Use meaningful names like `DEPLOY_ENV`, `APP_VERSION`  
- Store secrets using Jenkins **credentials**, not plain text  
- Print variables *only* for debugging (avoid showing passwords)  
- Combine environment variables with **parameters** for dynamic pipelines  

---

## 📘 Example Jenkinsfile

```
pipeline {
    agent any
    environment {
        APP_NAME = 'python-app'
        ENV_TYPE = 'QA'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building ${APP_NAME} for ${ENV_TYPE} environment"
            }
        }
    }
}
```

---

## 🧩 Summary

| Type         | Scope               | Example                    |
|---------------|---------------------|----------------------------|
| Built-in      | Provided by Jenkins | `$BUILD_NUMBER`, `$WORKSPACE` |
| Global        | All jobs            | `$ENV_TYPE`, `$ORG_NAME`   |
| Job-specific  | Single job          | `$APP_VERSION`             |
| Pipeline      | Inside Jenkinsfile  | `${APP_NAME}`              |
| Credentials   | Secure login info   | `${DOCKER_USER}`, `${DOCKER_PASS}` |

---

## 🚀 Conclusion

Environment variables are the **backbone** of dynamic Jenkins pipelines.  
They help you build **flexible**, **secure**, and **maintainable** CI/CD workflows — whether for Docker, Python, or cloud deployments.

---

