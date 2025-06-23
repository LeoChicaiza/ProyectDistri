package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8013/health")
    if err != nil {
        t.Fatalf("Error making request to parking-slots-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for parking-slots-service, got %d", resp.StatusCode)
    }
}
