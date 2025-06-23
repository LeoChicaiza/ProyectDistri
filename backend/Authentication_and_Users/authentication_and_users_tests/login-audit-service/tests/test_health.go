package tests

import (
    "net/http"
    "testing"
)

func TestHealthCheck(t *testing.T) {
    resp, err := http.Get("http://localhost:5000/health")
    if err != nil {
        t.Fatalf("Failed to reach login-audit-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected 200 OK from login-audit-service, got %d", resp.StatusCode)
    }
}
