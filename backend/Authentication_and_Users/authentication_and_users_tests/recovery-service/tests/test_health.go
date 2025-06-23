package tests

import (
    "net/http"
    "testing"
)

func TestHealthCheck(t *testing.T) {
    resp, err := http.Get("http://localhost:8005/health")
    if err != nil {
        t.Fatalf("Failed to reach recovery-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected 200 OK from recovery-service, got %d", resp.StatusCode)
    }
}
