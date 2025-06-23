FROM rust:1.76 as builder
WORKDIR /usr/src/app
COPY . .
RUN cargo build --release

FROM debian:bullseye-slim
WORKDIR /app
COPY --from=builder /usr/src/app/target/release/notification-service-ws .
COPY .env .env
EXPOSE 8026
CMD ["./notification-service-ws"]

