package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8014/health")
    if err != nil {
        t.Fatalf("Error making request to slot-maintenance-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for slot-maintenance-service, got %d", resp.StatusCode)
    }
}
