use warp::Filter;
use dotenv::dotenv;
use std::env;

mod ws;

#[tokio::main]
async fn main() {
    dotenv().ok();
    let port: u16 = env::var("PORT").unwrap_or_else(|_| "8026".to_string()).parse().unwrap();

    let ws_route = warp::path("ws")
        .and(warp::ws())
        .map(|ws: warp::ws::Ws| ws.on_upgrade(ws::handle_connection));

    println!("🚀 Notification WebSocket running on port {}", port);
    warp::serve(ws_route).run(([0, 0, 0, 0], port)).await;
}
