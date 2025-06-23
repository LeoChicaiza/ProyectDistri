
package handlers

import (
    "encoding/json"
    "net/http"
    "time"
)

type HealthStatus struct {
    Status  string    `json:"status"`
    Checked time.Time `json:"checked"`
}

func HealthCheck(w http.ResponseWriter, r *http.Request) {
    status := HealthStatus{
        Status:  "ok",
        Checked: time.Now(),
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(status)
}

type LogEntry struct {
    Message string `json:"message"`
    Time    string `json:"time"`
}

func GetLogs(w http.ResponseWriter, r *http.Request) {
    logs := []LogEntry{
        {Message: "System initialized", Time: time.Now().Add(-2 * time.Hour).Format(time.RFC3339)},
        {Message: "Heartbeat OK", Time: time.Now().Format(time.RFC3339)},
    }
    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(logs)
}
