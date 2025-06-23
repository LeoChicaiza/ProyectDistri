package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8015/health")
    if err != nil {
        t.Fatalf("Error making request to zones-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for zones-service, got %d", resp.StatusCode)
    }
}
