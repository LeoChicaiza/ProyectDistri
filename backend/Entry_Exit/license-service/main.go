package main

import (
	"fmt"
	"net/http"
	"os"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {

	err := godotenv.Load()
	if err != nil {
		fmt.Println("No .env file found, using system environment variables")
	}

	InitRedis()

	router := gin.Default()

	router.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "ok"})
	})

	router.POST("/recognize", func(c *gin.Context) {
		type Request struct {
			LicensePlate string `json:"license_plate"`
		}

		var req Request
		if err := c.BindJSON(&req); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid request"})
			return
		}

		timestamp := time.Now().Format(time.RFC3339)
		key := "plate:" + req.LicensePlate

		err := RedisClient.HSet(ctx, key, map[string]interface{}{
			"last_seen": timestamp,
		}).Err()
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to store plate info"})
			return
		}

		c.JSON(http.StatusOK, gin.H{
			"message":   "Plate recorded",
			"timestamp": timestamp,
		})
	})

	// Endpoint para consultar datos de una placa
	router.GET("/plate/:plate", func(c *gin.Context) {
		plate := c.Param("plate")
		key := "plate:" + plate

		result, err := RedisClient.HGetAll(ctx, key).Result()
		if err != nil || len(result) == 0 {
			c.JSON(http.StatusNotFound, gin.H{"error": "Plate not found"})
			return
		}

		c.JSON(http.StatusOK, result)
	})

	// Puerto desde variable de entorno o por defecto 8017
	port := os.Getenv("PORT")
	if port == "" {
		port = "8017"
	}

	// Iniciar servidor
	router.Run(":" + port)
}
