# Dockerfile

# Build Stage
FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package

# Run Stage
FROM openjdk:17-slim
WORKDIR /app
COPY --from=build /app/target/java-web-1.0-SNAPSHOT-jar-with-dependencies.jar app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
