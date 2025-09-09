void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop()
{
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(11, HIGH);
  delay(1000); // Wait for 90 millisecond(s)
  // turn the LED off by making the voltage LOW
  digitalWrite(11, LOW);
  delay(1000); // Wait for 90 millisecond(s)
}
