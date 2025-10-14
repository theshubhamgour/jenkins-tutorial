# Python Application CI/CD Demo with Jenkins and Docker

This repository contains a Jenkins pipeline setup for building, testing, and deploying a Python application using Docker on a worker node (`worker-noder`) for a demo. The pipeline is defined in the provided `Jenkinsfile`. Below is the guide to resolve Docker build issues encountered on the worker node.

## Problem Description
When running the `Docker Build` stage on the worker node (`worker-noder`), the following errors occur:

1. **Deprecated Builder Warning**:
   ```
   DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
   Install the buildx component to build images with BuildKit:
   https://docs.docker.com/go/buildx/
   ```

2. **Permission Denied Error**:
   ```
   permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock
   ```

These errors indicate:
- The legacy Docker builder is outdated; Docker Buildx should be used.
- The Jenkins user lacks permission to access the Docker daemon socket (`/var/run/docker.sock`).

## Solution

### 1. Install Docker Buildx
Install the Docker Buildx plugin on the worker node to replace the legacy builder.

#### Steps:
On the worker node (`worker-noder`), run as `root` or with `sudo`:
```bash
mkdir -p ~/.docker/cli-plugins
curl -sSL https://github.com/docker/buildx/releases/download/v0.17.1/buildx-v0.17.1.linux-amd64 -o ~/.docker/cli-plugins/docker-buildx
chmod +x ~/.docker/cli-plugins/docker-buildx
```

Verify installation:
```bash
docker buildx version
```

#### Update Jenkinsfile
Update the `Docker Build` stage in the `Jenkinsfile` to use Buildx. Replace:
```groovy
sh 'docker build -t python-app:latest .'
```
with:
```groovy
sh 'docker buildx build -t python-app:latest .'
```

### 2. Fix Docker Daemon Permission
The Jenkins user lacks permission to access `/var/run/docker.sock`. Add the Jenkins user to the `docker` group.

#### Steps:
1. Identify the Jenkins user (e.g., `jenkins` or `ubuntu`).
2. Add the user to the `docker` group:
   ```bash
   sudo usermod -aG docker <jenkins-user>
   ```
   Replace `<jenkins-user>` with the actual user.

3. Restart the worker node to apply changes:
   ```bash
   sudo reboot
   ```

## Demo Setup
The `Jenkinsfile` defines a pipeline with the following stages:
1. **Clone Github Repository**: Clones the `main` branch from `https://github.com/theshubhamgour/jenkins-tutorial.git`.
2. **Build**: Compiles the Python application (`app.py`) in `4-python-jenkins-docker-app`.
3. **Test**: Runs unit tests in the `tests` directory.
4. **Docker Build**: Builds a Docker image (`python-app:latest`) using the `Dockerfile`.
5. **Docker Run**: Runs the Docker image in a container.
6. **Docker Tag & Push**: Logs into Docker Hub, tags the image, and pushes it to `theshubhamgour/python-app:latest`.

## Prerequisites
- Jenkins installed with a worker node (`worker-node`).
- Docker installed on the worker node.
- `Jenkinsfile`, `Dockerfile`, `app.py`, and `tests` directory in the repository.
- Docker Hub credentials stored in Jenkins with ID `theshubhamgour`.

## Running the Demo
1. Ensure the worker node (`worker-node`) is online.
2. Trigger the pipeline in Jenkins.
3. Verify the Docker image:
   ```bash
   docker images | grep python-app
   ```

## Troubleshooting
- **Buildx Installation Fails**: Ensure `curl` is installed (`sudo apt-get install curl`) and verify the download URL.
- **Permission Denied Persists**: Check if the Jenkins user is in the `docker` group (`groups <jenkins-user>`).
- **File Access Errors**: Ensure the workspace directory (`/home/ubuntu/workspace/Python_application_cicd/4-python-jenkins-docker-app/`) and `Dockerfile` are accessible:
  ```bash
  sudo chown -R <jenkins-user>:<jenkins-user> /home/ubuntu/workspace/Python_application_cicd
  sudo chmod -R u+rw /home/ubuntu/workspace/Python_application_cicd
  ```

## References
- [Docker Buildx Documentation](https://docs.docker.com/go/buildx/)
- [Docker Daemon Permissions](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
