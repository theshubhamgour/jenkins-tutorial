# Declarative Pipeline

This directory contains examples of Jenkins Declarative Pipelines. Declarative Pipeline is a more recent and structured way to define your continuous delivery pipelines in Jenkins. It offers a simplified and more opinionated syntax compared to Scripted Pipelines, making it easier to write and read.

## `jenkinsfile-declarative`

This file provides a basic example of a Declarative Pipeline. Let's break down its structure:

```groovy
pipeline {
    agent any

    stages {
        stage("Build") {
            steps {
                // Run build commands
                sh 'echo "Building project..."'
            }
        }

        stage("Test") {
            steps {
                // Run tests
                sh 'echo "Running tests..."'
            }
        }

        stage("Deploy") {
            steps {
                // Deploy step (dummy for now)
                sh 'echo "Deploying application..."'
            }
        }
    }
}
```

### Key Concepts

*   **`pipeline` block:** This is the main block that encloses the entire pipeline definition.
*   **`agent` directive:** This specifies where the entire Pipeline, or a specific stage, will execute in the Jenkins environment. `agent any` means that Jenkins can use any available agent to run the pipeline.
*   **`stages` block:** This block contains one or more `stage` blocks, which are the main sections of your pipeline. Each stage represents a distinct part of your delivery process, such as "Build", "Test", or "Deploy".
*   **`stage` block:** This defines a specific stage in the pipeline. Each stage is given a name that is displayed in the Jenkins UI.
*   **`steps` block:** This block contains the actual commands to be executed in a stage. In this example, we are using the `sh` step to execute a shell command (`echo`).

## `jenkinsfile-declarative-ws`

This file demonstrates the use of the `ws` (workspace) step in a Declarative Pipeline. The `ws` step allows you to execute a set of steps in a specific directory within the Jenkins workspace. This is useful for organizing your build artifacts and ensuring that your steps are executed in the correct context.

This example will be added in a future update.


