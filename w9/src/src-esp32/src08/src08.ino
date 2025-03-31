#include "DHT.h"

#include <WiFi.h>
#include <HTTPClient.h>
#include <Arduino_JSON.h>

int dhtPin = 26;
DHT dht(dhtPin, DHT11);

const char* ssid = "AIOTTANWK";
const char* password = "Password1!";

// IP address
String host = "192.168.137.1:5000";



void setup() {

  Serial.begin(115200);
  randomSeed(analogRead(0));
  // dht.begin();

  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {

  // float temp = dht.readTemperature();

  float temp = random(2000, 4000) * 0.01;
  Serial.println("Temp: " + String(temp));

  WiFiClient client;
  HTTPClient http;
  http.begin(client, "http://" + host + "/api/sensor?temperature=" + String(temp));
  http.addHeader("Content-Type", "text/plain");
  int httpResponseCode = http.PUT("");
  
  if(httpResponseCode>0)
  {
    String response = http.getString();
    Serial.println(httpResponseCode);

    JSONVar myObject = JSON.parse(response);
    JSONVar value = myObject["temperature"];
    Serial.println(value);
  }
  else
  {
    Serial.print("Error on sending PUT: ");
    Serial.println(httpResponseCode);
  }
  
  http.end();
  
  delay(1000);
}
