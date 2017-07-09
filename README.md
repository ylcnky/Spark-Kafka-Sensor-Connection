## IoT Sensor Data Streaming Simulation with Spark+Kafka

This code simulates the connection between an IoT server (physical or cloud-based) and a client pc.
You can either use in local Spark or in any Hadoop distro VM.

To run the program download the `streaming` jar file and run this command `spark-submit --jars spark-streaming-kafka-0-8-assembly_2.11-2.0.0-preview.jar  \
./kafka-direct-iotmsg.py localhost:9092 iotmsgs`
