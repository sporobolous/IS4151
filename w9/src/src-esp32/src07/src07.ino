#include "DHT.h"

int dhtPin = 26;
DHT dht(dhtPin, DHT11);

void setup() {

  Serial.begin(115200);
  dht.begin();  
}

void loop() {

  float temp = dht.readTemperature();
  Serial.println("Temp: " + String(temp));
  
  delay(1000);
}
