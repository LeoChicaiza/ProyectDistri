package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8018/health")
    if err != nil {
        t.Fatalf("Failed to connect to service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected status 200, got %d", resp.StatusCode)
    }
}
