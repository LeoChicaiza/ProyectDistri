package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8012/health")
    if err != nil {
        t.Fatalf("Error making request to parking-lot-creation-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for parking-lot-creation-service, got %d", resp.StatusCode)
    }
}
