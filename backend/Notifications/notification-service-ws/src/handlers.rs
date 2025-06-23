use axum::{
    extract::WebSocketUpgrade,
    response::IntoResponse,
    response::Response,
};
use axum::extract::ws::{WebSocket, Message};
use futures::{SinkExt, StreamExt};

pub async fn ws_handler(ws: WebSocketUpgrade) -> Response {
    ws.on_upgrade(handle_socket)
}

async fn handle_socket(mut socket: WebSocket) {
    while let Some(Ok(msg)) = socket.next().await {
        if let Message::Text(text) = msg {
            println!("📨 Received: {}", text);
            let _ = socket.send(Message::Text(format!("Echo: {}", text))).await;
        }
    }
}
