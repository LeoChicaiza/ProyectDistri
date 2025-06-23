package main

import (
	"net/http"
	"os"

	"control-service/redisutil"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
)

func main() {
	// Cargar archivo .env
	if err := godotenv.Load(); err != nil {
		println("⚠️ No .env file found, using defaults")
	}

	// Crear cliente de Redis
	client := redisutil.NewRedisClient()

	r := gin.Default()

	r.GET("/health", func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{"status": "UP", "service": "control-service"})
	})

	// Endpoint para obtener último movimiento de un vehículo
	r.GET("/control/:plate", func(c *gin.Context) {
		plate := c.Param("plate")
		keys := []string{
			"entry:" + plate,
			"exit:" + plate,
			"plate:" + plate,
		}

		data := make(map[string]map[string]string)

		for _, key := range keys {
			val, err := client.HGetAll(redisutil.Ctx, key).Result()
			if err == nil && len(val) > 0 {
				data[key] = val
			}
		}

		if len(data) == 0 {
			c.JSON(http.StatusNotFound, gin.H{"error": "No data found"})
			return
		}

		c.JSON(http.StatusOK, data)
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8020"
	}

	r.Run(":" + port)
}
