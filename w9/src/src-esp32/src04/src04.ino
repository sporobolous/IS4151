int buttonPin = 26;

void setup() {

  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
  
}

void loop() {
  
  if(digitalRead(buttonPin) == HIGH)
  {
     Serial.println("Button Released");
  }
  else
  {
    Serial.println("Button Pressed");
  }

  delay(100);
}
