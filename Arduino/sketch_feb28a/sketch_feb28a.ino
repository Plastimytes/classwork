const int buzzerPin = 8;

void setup() {
  // Set the buzzer
  pinMode(buzzerPin, OUTPUT);

}

void loop() {
  // Turn the buzzer
  digitalWrite(buzzerPin, HIGH);
  delay(1500);

    // Turn the buzzer
  digitalWrite(buzzerPin, LOW);
  delay(1500);
}


