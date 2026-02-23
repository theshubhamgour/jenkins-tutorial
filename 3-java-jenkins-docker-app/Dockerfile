# Use OpenJDK base image
# Full JDK via Eclipse Temurin
FROM eclipse-temurin:17-jdk     


WORKDIR /app

COPY target/java-jenkins-docker-1.0-SNAPSHOT.jar app.jar

ENTRYPOINT ["java", "-jar", "app.jar"]
