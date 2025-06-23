# Dockerfile entry-service
FROM golang:1.20-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o entry-service .

# Etapa final liviana
FROM alpine:3.18
WORKDIR /app
COPY --from=builder /app/entry-service .
COPY --from=builder /app/.env .  

EXPOSE 8018
CMD ["./entry-service"]
