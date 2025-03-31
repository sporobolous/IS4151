int buttonPin = 26;
int ledPin = 25;
int ledState;

void setup() {

  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);

  ledState = LOW;
}

void loop() {
  
  if(digitalRead(buttonPin) == LOW)
  {
     if(ledState == LOW)
     {
      ledState = HIGH;
     }
     else
     {
      ledState = LOW;
     }

     digitalWrite(ledPin, ledState);
  }  

  delay(100);
}
