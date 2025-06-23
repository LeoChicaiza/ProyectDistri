package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/go-redis/redis/v8"

	"github.com/gin-gonic/gin"

	"github.com/joho/godotenv"
)

var (
	ctx         = context.Background()
	RedisClient *redis.Client
)

func InitRedis() {
	redisHost := os.Getenv("REDIS_HOST")
	redisPort := os.Getenv("REDIS_PORT")
	addr := fmt.Sprintf("%s:%s", redisHost, redisPort)

	RedisClient = redis.NewClient(&redis.Options{
		Addr: addr,
		DB:   0,
	})

	_, err := RedisClient.Ping(ctx).Result()
	if err != nil {
		panic("No se pudo conectar a Redis: " + err.Error())
	}

	fmt.Println("Conectado a Redis")
}

func main() {
	err := godotenv.Load()
	if err != nil {
		fmt.Println("No se encontró .env, usando valores por defecto")
	}

	InitRedis()

	router := gin.Default()

	router.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok"})
	})

	router.POST("/entry", func(c *gin.Context) {
		type EntryRequest struct {
			LicensePlate string `json:"license_plate"`
		}

		var req EntryRequest
		if err := c.BindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Petición inválida"})
			return
		}

		timestamp := time.Now().Format(time.RFC3339)
		key := "entry:" + req.LicensePlate

		err := RedisClient.HSet(ctx, key, map[string]interface{}{
			"entered_at": timestamp,
		}).Err()
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "No se pudo registrar entrada"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"message": "Entrada registrada", "timestamp": timestamp})
	})

	router.GET("/entry/:plate", func(c *gin.Context) {
		plate := c.Param("plate")
		key := "entry:" + plate

		result, err := RedisClient.HGetAll(ctx, key).Result()
		if err != nil || len(result) == 0 {
			c.JSON(http.StatusNotFound, gin.H{"error": "No se encontró la entrada"})
			return
		}

		c.JSON(http.StatusOK, result)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8018"
	}

	router.Run(":" + port)
}
