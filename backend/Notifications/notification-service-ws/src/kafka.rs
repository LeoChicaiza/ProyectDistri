use std::env;
use rdkafka::consumer::{Consumer, StreamConsumer};
use rdkafka::config::ClientConfig;
use rdkafka::message::Message;
use tokio_stream::StreamExt;

pub async fn consume_events() {
    let brokers = env::var("KAFKA_BROKERS").unwrap_or("localhost:9092".into());
    let topic = env::var("KAFKA_TOPIC").unwrap_or("parking_notifications".into());

    let consumer: StreamConsumer = ClientConfig::new()
        .set("group.id", "notification-group")
        .set("bootstrap.servers", &brokers)
        .create()
        .expect("Failed to create Kafka consumer");

    consumer.subscribe(&[&topic]).expect("Can't subscribe");

    println!("📡 Listening for Kafka messages on topic: {}", topic);

    let mut stream = consumer.stream();
    while let Some(message) = stream.next().await {
        match message {
            Ok(m) => {
                if let Some(payload) = m.payload_view::<str>().ok().flatten() {
                    println!("🔔 Notification received: {}", payload);
                }
            }
            Err(e) => eprintln!("Kafka error: {:?}", e),
        }
    }
}
