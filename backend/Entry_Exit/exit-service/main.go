package main

import (
	"context"
	"fmt"
	"net/http"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis/v8"
	"github.com/joho/godotenv"
)

var ctx = context.Background()
var redisClient *redis.Client

func main() {
	godotenv.Load()
	InitRedis()

	router := gin.Default()

	router.POST("/exit", func(c *gin.Context) {
		var req struct {
			Plate     string `json:"plate"`
			Timestamp string `json:"timestamp"`
		}

		if err := c.BindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON"})
			return
		}

		key := "exit:" + req.Plate
		err := redisClient.HSet(ctx, key, map[string]interface{}{
			"last_exit": req.Timestamp,
		}).Err()
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to store exit"})
			return
		}

		fmt.Println("Evento: salida registrada para placa:", req.Plate)
		c.JSON(http.StatusOK, gin.H{"message": "Exit registered", "timestamp": req.Timestamp})
	})

	router.GET("/exit/:plate", func(c *gin.Context) {
		plate := c.Param("plate")
		key := "exit:" + plate

		result, err := redisClient.HGetAll(ctx, key).Result()
		if err != nil || len(result) == 0 {
			c.JSON(http.StatusNotFound, gin.H{"error": "No exit info found"})
			return
		}

		c.JSON(http.StatusOK, result)
	})

	router.GET("/health", func(c *gin.Context) {
		c.String(http.StatusOK, "exit-service up")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8019"
	}

	router.Run(":" + port)
}
