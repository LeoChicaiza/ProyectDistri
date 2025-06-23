
package main

import (
    "log"
    "net/http"
    "health-monitoring-service/handlers"
)

func main() {
    http.HandleFunc("/health", handlers.HealthCheck)
    http.HandleFunc("/logs", handlers.GetLogs)

    log.Println("Health Monitoring Service running on port 8028...")
    log.Fatal(http.ListenAndServe(":8028", nil))
}
