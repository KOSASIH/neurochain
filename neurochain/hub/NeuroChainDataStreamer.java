import org.apache.kafka.streams.KafkaStreams;
import org.apache.kafka.streams.StreamsBuilder;
import org.apache.kafka.streams.kstream.KStream;

public class NeuroChainDataStreamer {
    public static void main(String[] args) {
        StreamsBuilder builder = new StreamsBuilder();
        KStream<String, String> stream = builder.stream("neurochain_topic");
        stream.foreach((key, value) -> System.out.println("Received message: " + value));
        KafkaStreams streams = new KafkaStreams(builder.build(), new StreamsConfig());
        streams.start();
    }
}
