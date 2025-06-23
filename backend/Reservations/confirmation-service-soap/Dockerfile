
FROM maven:3.8.6-openjdk-17 AS build
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

FROM openjdk:17-jdk
WORKDIR /app
COPY --from=build /app/target/confirmation-service-1.0.0.jar app.jar
EXPOSE 8030
ENTRYPOINT ["java", "-jar", "app.jar"]
