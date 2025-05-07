import paho.mqtt.client as mqtt

HOST = "10.8.21.61"
PORT = 1883
TOPIC = "counter/value"

last_message = ""


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe(TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global last_message
    last_message = msg.payload.decode("utf-8")[-2]


def on_subscribe(client, userdata, mid, reason_code_list, properties):
    # Since we subscribed only for a single channel, reason_code_list contains
    # a single entry
    if reason_code_list[0].is_failure:
        print(f"Broker rejected you subscription: {reason_code_list[0]}")
    else:
        print(f"Broker granted the following QoS: {reason_code_list[0].value}")


def init():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message
    mqttc.on_subscribe = on_subscribe

    mqttc.connect(HOST, PORT)

    mqttc.loop_start()


def get_last_message():
    return last_message
