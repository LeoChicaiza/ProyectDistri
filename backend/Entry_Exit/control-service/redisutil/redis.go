package redisutil

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/go-redis/redis/v8"
)

var Ctx = context.Background()

func NewRedisClient() *redis.Client {
	host := os.Getenv("REDIS_HOST")
	if host == "" {
		host = "localhost"
	}

	port := os.Getenv("REDIS_PORT")
	if port == "" {
		port = "6379"
	}

	addr := fmt.Sprintf("%s:%s", host, port)

	client := redis.NewClient(&redis.Options{
		Addr:        addr,
		DialTimeout: 5 * time.Second,
		ReadTimeout: 3 * time.Second,
	})

	_, err := client.Ping(Ctx).Result()
	if err != nil {
		panic(fmt.Sprintf("Error connecting to Redis: %v", err))
	}

	fmt.Println("Redis connected successfully")
	return client
}
