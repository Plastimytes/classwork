//Light up Three LEDs at Different intervals
void setup()
{
  pinMode(11, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(A2, OUTPUT);
}

void loop()
{
  //Green LED
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(11, HIGH);
  delay(1000); // Wait for 1000 millisecond(s)
  // turn the LED off by making the voltage LOW
  digitalWrite(11, LOW);
  delay(1000); // Wait for 1000 millisecond(s)

  //Red LED
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(7, HIGH);
  delay(500); // Wait for 500 millisecond(s)
  // turn the LED off by making the voltage LOW
  digitalWrite(7, LOW);
  delay(500); // Wait for 500 millisecond(s)

  //Orange LED
  // turn the LED on (HIGH is the voltage level)
  digitalWrite(A2, HIGH);
  delay(250); // Wait for 250 millisecond(s)
  // turn the LED off by making the voltage LOW
  digitalWrite(A2, LOW);
  delay(1000); // Wait for 1000 millisecond(s)


}
