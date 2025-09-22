# Jenkins Pipelines Tutorial

This directory contains examples and explanations for Jenkins Pipelines, demonstrating both Declarative and Scripted Pipeline syntaxes. Jenkins Pipelines are a suite of plugins that supports implementing and integrating continuous delivery pipelines into Jenkins. They provide an extensible set of tools for modeling simple to complex delivery pipelines 'as code'.

## What is a Jenkins Pipeline?

A Jenkins Pipeline is a collection of plugins that allows you to implement and integrate continuous delivery pipelines into Jenkins. A continuous delivery pipeline is an automated expression of your process for getting software from version control to your users. Every change to your software (committed in source control) goes through a complex process on its way to being released. This process involves building the software, running tests, and deploying it to various environments. Jenkins Pipeline provides a robust, durable, and extensible automation server that can orchestrate this entire process.

Key characteristics of Jenkins Pipelines:

*   **Code:** Pipelines are implemented in code, typically stored in a `Jenkinsfile` in your project's source control repository. This allows for versioning, auditing, and collaboration on your delivery process.
*   **Durable:** Pipelines can survive planned and unplanned restarts of the Jenkins controller. This means that even if your Jenkins instance goes down during a long-running build, it will resume from where it left off once Jenkins is back online.
*   **Pausable:** Pipelines can optionally stop and wait for human input or approval before continuing the Pipeline run.
*   **Extensible:** Pipelines can be extended by developers and users to support their project's specific needs.
*   **Versatile:** Pipelines are capable of modeling complex real-world continuous delivery processes, including parallel execution, conditional logic, and integration with various tools.

## Declarative vs. Scripted Pipelines

Jenkins offers two distinct syntaxes for creating Pipelines: Declarative and Scripted. Both are powerful ways to implement continuous delivery pipelines, but they differ significantly in their structure and flexibility.

### Declarative Pipeline

Declarative Pipeline is a more recent and opinionated way to create Jenkins Pipelines. It provides a simpler, more structured syntax designed for ease of use and readability. Declarative Pipelines are defined within a `pipeline` block in a `Jenkinsfile` and typically follow a predefined structure with `agent`, `stages`, and `steps` sections. It's often preferred for simpler, more straightforward continuous delivery scenarios due to its enforced structure and clear syntax.

### Scripted Pipeline

Scripted Pipeline, built on Groovy, offers a much more flexible and powerful way to define pipelines. It's essentially a general-purpose programming environment within Jenkins, allowing for complex logic, custom functions, and tight integration with Groovy's capabilities. Scripted Pipelines are defined within a `node` block and offer greater control over the pipeline's execution flow. They are typically used for more complex or highly customized continuous delivery processes where the structured nature of Declarative Pipeline might be too restrictive.

This tutorial will explore both types of pipelines, providing examples and explanations to help you understand their differences and when to use each. You will find dedicated subdirectories for `declarative-pipeline` and `scripted-pipeline`, each containing their respective `Jenkinsfile` examples and detailed READMEs.

