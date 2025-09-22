# Scripted Pipeline

This directory contains examples of Jenkins Scripted Pipelines. Scripted Pipeline is a powerful and flexible way to define your continuous delivery pipelines using Groovy-based scripting. It offers a high degree of control over the pipeline's execution flow and allows for complex logic and custom functions.

## `jenkinsfile-scripted`

This file provides a basic example of a Scripted Pipeline. Let's break down its structure:

```groovy
node {
    stage('Build') {
        // Run build commands
        sh 'echo "Building project..."'
    }
    stage('Test') {
        // Run tests
        sh 'echo "Running tests..."'
    }
    stage('Deploy') {
        sh 'echo "Deploying application..."'
    }
}
```

### Key Concepts

*   **`node` block:** This is the fundamental block in a Scripted Pipeline. It allocates an executor on a Jenkins agent and runs the enclosed steps within the workspace of that agent. All steps in a Scripted Pipeline typically run inside a `node` block.
*   **`stage` block:** Similar to Declarative Pipelines, `stage` blocks are used to organize the pipeline into logical sections. While not strictly enforced in Scripted Pipeline as in Declarative, it's a best practice to use stages for better visualization in the Jenkins UI.
*   **Steps:** Inside the `stage` blocks, you define the actual steps to be executed. These can be shell commands (`sh`), Groovy code, or other Jenkins Pipeline steps.

## `jenkinsfile-scripted-ws`

This file demonstrates the use of the `ws` (workspace) step in a Scripted Pipeline. The `ws` step allows you to execute a set of steps in a specific directory within the Jenkins workspace. This is useful for organizing your build artifacts and ensuring that your steps are executed in the correct context.

This example will be added in a future update.


