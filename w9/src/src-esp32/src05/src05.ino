int buttonPin = 26;
int buttonState;

void setup() {

  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);

  buttonState = LOW;
}

void loop() {
  
  if(digitalRead(buttonPin) == LOW)
  {
     if(buttonState == LOW)
     {
      buttonState = HIGH;
     }
     else
     {
      buttonState = LOW;
     }
  }

  Serial.println("buttonState: " + String(buttonState));

  delay(100);
}
