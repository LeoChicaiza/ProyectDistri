package tests

import (
    "net/http"
    "testing"
)

func TestHealth(t *testing.T) {
    resp, err := http.Get("http://localhost:8011/health")
    if err != nil {
        t.Fatalf("Failed to connect: %v", err)
    }
    if resp.StatusCode != http.StatusOK {
        t.Fatalf("Expected status 200, got %d", resp.StatusCode)
    }
}
