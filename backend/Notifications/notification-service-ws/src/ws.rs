use warp::ws::{Message, WebSocket};
use futures::{SinkExt, StreamExt};

pub async fn handle_connection(ws: WebSocket) {
    let (mut tx, mut rx) = ws.split();

    while let Some(result) = rx.next().await {
        if let Ok(msg) = result {
            if msg.is_text() {
                println!("Received: {:?}", msg.to_str());
                tx.send(Message::text("Message received")).await.unwrap();
            }
        }
    }
}
