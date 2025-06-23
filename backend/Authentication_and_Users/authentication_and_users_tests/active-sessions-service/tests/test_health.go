package tests

import (
    "net/http"
    "testing"
)

func TestHealthCheck(t *testing.T) {
    resp, err := http.Get("http://localhost:8003/health")
    if err != nil {
        t.Fatalf("Failed to reach active-sessions-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected 200 OK from active-sessions-service, got %d", resp.StatusCode)
    }
}
