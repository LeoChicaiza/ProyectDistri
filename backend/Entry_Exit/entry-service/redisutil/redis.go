package redisutil

import (
	"context"
	"fmt"
	"os"
	"time"

	"github.com/go-redis/redis/v8"
)

var (
	Ctx         = context.Background()
	RedisClient *redis.Client
)

// Init initializes the Redis client and assigns it to RedisClient
func Init() {
	addr := os.Getenv("REDIS_ADDR")
	if addr == "" {
		addr = "localhost:6379"
	}

	RedisClient = redis.NewClient(&redis.Options{
		Addr:        addr,
		DialTimeout: 5 * time.Second,
		ReadTimeout: 3 * time.Second,
	})

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()

	if _, err := RedisClient.Ping(ctx).Result(); err != nil {
		panic(fmt.Errorf("❌ Redis connection failed: %w", err))
	}

	fmt.Println("✅ Redis connection established")
}
