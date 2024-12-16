from kafka import KafkaProducer
import json
import random
import time

# Kafka 설정
BROKER = 'localhost:9092'  # DCIM Kafka 브로커 주소
# TOPIC = 'equipment_sensor_data'
TOPIC = 'dcim-topic'

# Kafka Producer 생성
producer = KafkaProducer(
    bootstrap_servers=BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# 장비 목록
equipment_ids = [f"{str(i).zfill(5)}" for i in range(1, 11)]


def generate_sensor_data():
    """임의의 온도와 습도 데이터를 생성"""
    equipment_id = random.choice(equipment_ids)
    temperature = round(random.uniform(20.0, 80.0), 2)  # 온도 범위
    humidity = round(random.uniform(30.0, 90.0), 2)  # 습도 범위
    timestamp = int(time.time() * 1000)  # 타임스탬프 (밀리초)

    data = {
        'equipment_id': equipment_id,
        'temperature': temperature,
        'humidity': humidity,
        'timestamp': timestamp
    }
    return data


# Kafka 데이터 전송 루프
try:
    print("데이터 전송 시작...")
    while True:
        sensor_data = generate_sensor_data()
        producer.send(TOPIC, value=sensor_data)
        print(f"전송된 데이터: {sensor_data}")
        time.sleep(5)  # 5초 간격으로 데이터 전송

except KeyboardInterrupt:
    print("데이터 전송 종료.")
finally:
    producer.close()
