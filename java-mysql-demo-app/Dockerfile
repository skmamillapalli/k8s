FROM openjdk:8-jdk-alpine
ARG JAR_FILE=target/java-app-vault-secret-demo-0.0.1-SNAPSHOT.jar
COPY ${JAR_FILE} app.jar
WORKDIR /vault/secrets
ENTRYPOINT ["java","-jar","/app.jar","-Dspring.config.location=application.properties"]