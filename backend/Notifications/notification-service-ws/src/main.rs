mod handlers;
mod kafka;

use axum::{routing::get, Router};
use dotenv::dotenv;
use std::env;
use std::net::SocketAddr;

#[tokio::main]
async fn main() {
    dotenv().ok();
    env_logger::init();

    let kafka_task = tokio::spawn(kafka::consume_events());

    let app = Router::new().route("/ws", get(handlers::ws_handler));

    let port = env::var("PORT").unwrap_or_else(|_| "8026".to_string());
    let addr = format!("0.0.0.0:{}", port).parse::<SocketAddr>().unwrap();
    println!("✅ Listening on {}", addr);

    axum::Server::bind(&addr)
        .serve(app.into_make_service())
        .await
        .unwrap();

    kafka_task.await.unwrap();
}

