package main

import (
    "context"
    "os"

    "github.com/go-redis/redis/v8"
)

var ctx = context.Background()
var RedisClient *redis.Client

func InitRedis() {
    RedisClient = redis.NewClient(&redis.Options{
        Addr:     os.Getenv("REDIS_ADDR"),
        Password: os.Getenv("REDIS_PASSWORD"),
        DB:       0,
    })
}
