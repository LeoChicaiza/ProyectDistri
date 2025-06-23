package tests

import (
    "net/http"
    "testing"
)

func TestHealthCheck(t *testing.T) {
    resp, err := http.Get("http://localhost:8002/health")
    if err != nil {
        t.Fatalf("Failed to reach access-control-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected 200 OK from access-control-service, got %d", resp.StatusCode)
    }
}
