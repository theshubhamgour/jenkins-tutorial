# Java Jenkins Docker Tutorial

## Run Locally
```bash
mvn clean package
java -jar target/java-jenkins-docker-1.0-SNAPSHOT.jar
```

## Run with Docker
```bash
docker build -t java-jenkins-docker:latest .
docker run --rm java-jenkins-docker:latest
```

## Run with Docker Compose
```bash
docker-compose up --build
```
