// Define pin numbers
const int pirSensorPin = 8;   // PIR sensor input
const int motor1Pin = 7;          //Motor 1 pin
const int motor2Pin = 6;         // Motor 2 pin
const int led2Pin = 12;         // LED 2 pin
const int led3Pin = 13;         // LED 3 pin

const int button1Pin = 9;      // Button 1 pin (to turn off the first 3 LEDs)
const int button2Pin = 10;      // Button 2 pin (to turn on motor2 for 2 seconds)

unsigned long motor2Timer = 0;   // Timer for motor 2
bool pirDetected = false;      // PIR sensor state
bool motor2On = false;           // motor 2 state

void setup() {
  
  // Initialize pins
  pinMode(pirSensorPin, INPUT);
  pinMode(motor1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  pinMode(led3Pin, OUTPUT);
  pinMode(motor2Pin, OUTPUT);
  pinMode(button1Pin, INPUT_PULLUP);  // Button 1 (to turn off LEDs 1-3)
  pinMode(button2Pin, INPUT_PULLUP);  // Button 2 (to turn on motor2 for 2 seconds)

  // Initialize LEDs to off
  digitalWrite(motor1Pin, LOW);
  digitalWrite(led2Pin, LOW);
  digitalWrite(led3Pin, LOW);
  digitalWrite(motor2Pin, LOW);
}

void loop() {
  // Check PIR sensor state
  pirDetected = digitalRead(pirSensorPin);

  // If motion detected, turn on all LEDs
  if (pirDetected) {
    digitalWrite(motor1Pin, HIGH);
    digitalWrite(led2Pin, HIGH);
    digitalWrite(led3Pin, HIGH);
    digitalWrite(motor2Pin, HIGH);
    motor2Timer = millis();  // Start timer for motor 2
    motor2On = true;
    
  }

  // If 2 seconds passed after motion detection, turn off motor 2
  if (motor2On && millis() - motor2Timer >= 2000) {
    digitalWrite(motor2Pin, LOW);
    motor2On = false;
  }

  // Check button 1 (turn off LEDs 1, 2, and 3)
  if (digitalRead(button1Pin) == LOW) {
    digitalWrite(motor1Pin, LOW);
    digitalWrite(led2Pin, LOW);
    digitalWrite(led3Pin, LOW);
  }

  // Check button 2 (turn on LED 4 for 2 seconds)
  if (digitalRead(button2Pin) == LOW) {
    digitalWrite(motor2Pin, HIGH);
    delay(2000); // Keep LED 4 on for 2 seconds
    digitalWrite(motor2Pin, LOW);
  }
}
