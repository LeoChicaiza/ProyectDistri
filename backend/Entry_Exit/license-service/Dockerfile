FROM golang:1.20-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags="-s -w" -o license-service .

FROM alpine:3.18
WORKDIR /app
COPY --from=builder /app/license-service .
COPY --from=builder /app/.env .

# Instala dependencias para procesamiento de imágenes (si es necesario)
RUN apk add --no-cache tesseract-ocr

EXPOSE 8017
CMD ["./license-service"]

