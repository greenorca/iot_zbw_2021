import paho.mqtt.client as mqtt
import json
def handleIncomingMessages(client, userdata, message):
    data = json.loads(message.payload) #convert payload string to JSON
    print("Temp: ", data["temperature"])
    # send an alert in case of overheating
    if data["temperature"]>=30:
      topic = "alerts/"+message.topic.split("/")[-1]
      client.publish(topic, "holy cow!")
if __name__ == '__main__':
  client = mqtt.Client('meister_tux')
  client.connect("192.168.0.30", port=1883)
  client.subscribe("iot_zbw_sensor/#")
  client.on_message = handleIncomingMessages
  client.loop_forever()
