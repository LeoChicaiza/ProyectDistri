FROM rust:1.73 as builder

WORKDIR /usr/src/app
COPY . .
RUN cargo build --release

FROM debian:buster-slim
WORKDIR /app
COPY --from=builder /usr/src/app/target/release/notification-service-ws .

ENV PORT=8026
EXPOSE 8026

CMD ["./notification-service-ws"]
