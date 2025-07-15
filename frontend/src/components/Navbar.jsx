
import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "1rem", background: "#333", color: "#fff" }}>
      <Link to="/" style={{ marginRight: "1rem", color: "#fff" }}>Home</Link>
      <Link to="/dashboard" style={{ marginRight: "1rem", color: "#fff" }}>Dashboard</Link>
      <Link to="/login" style={{ color: "#fff" }}>Login</Link>
    </nav>
  );
}
