package main

import (
    "net/http"
    "testing"
)

func TestHealthEndpoint(t *testing.T) {
    resp, err := http.Get("http://localhost:8011/health")
    if err != nil {
        t.Fatalf("Error making request to levels-floors-service: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Errorf("Expected status 200 OK for levels-floors-service, got %d", resp.StatusCode)
    }
}
