package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8010/health")
    if err != nil {
        t.Fatalf("Error making request to availability-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for availability-service, got %d", resp.StatusCode)
    }
}
