// Define motor control pins
#define motor1Pin1  7 // IN1
#define motor1Pin2  6 // IN2
const int motor2Pin1 = 4; // IN3
const int motor2Pin2 = 5; // IN
const int enableA = 6;     // ENA
const int enableB = 7;     // ENB

// Define LED pins
const int led1Pin = 12; // LED 1 (Use a different pin for the LED)
const int led2Pin = 13; // LED 2 (Use a different pin for the LED)


// Define PIR sensor pin
const int pirPin = 8; // PIR sensor output pin

// Define button pins
const int buttonPin = 9; // Button to manually turn off LEDs
const int stopButtonPin = 10; // Button to stop the motors

// Variables to store button states
int buttonState = 0;
int stopButtonState = 0;

// Flag to track LED and motor states
bool ledsOn = false;
bool motorsRunning = false; // Motors are not running by default

void setup() {
  // Start the Serial communication
  Serial.begin(9600);
  
  // Set motor control pins as outputs
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);
  pinMode(enableA, OUTPUT);
  pinMode(enableB, OUTPUT);
  
  // Set LED pins as outputs
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  
  // Set PIR sensor pin as input
  pinMode(pirPin, INPUT);
  
  // Set button pins as input
  pinMode(buttonPin, INPUT);
  pinMode(stopButtonPin, INPUT);
  
  // Enable motors
  digitalWrite(enableA, HIGH);
  digitalWrite(enableB, HIGH);
}

void loop() {
  // Read the PIR sensor
  int pirState = digitalRead(pirPin);
  
  // Check if the button is pressed to turn off LEDs
  buttonState = digitalRead(buttonPin);
  
  // Check if the stop button is pressed to stop the motors
  stopButtonState = digitalRead(stopButtonPin);
  
  // If the stop button is pressed, stop the motors
  if (stopButtonState == HIGH && motorsRunning) {
    // Stop the motors
    digitalWrite(motor1Pin1, HIGH);
    digitalWrite(motor1Pin2, HIGH);
  
    motorsRunning = false;
    Serial.println("Stop button pressed: Motors ON");
    delay(2000);
  }

  // If the button is pressed, turn off the LEDs
  if (buttonState == HIGH && ledsOn) {
    digitalWrite(led1Pin, LOW);
    digitalWrite(led2Pin, LOW);
    ledsOn = false;  // Update LED status to off
    Serial.println("Button pressed: LEDs OFF");
  }

  // If motion is detected and LEDs are not already on
  if (pirState == HIGH && !ledsOn) {
    Serial.println("Motion detected!");
    
    // Turn on LED 1
    digitalWrite(led1Pin, HIGH);
    Serial.println("LED 1 ON");
    
    // Turn off LED 2
    digitalWrite(led2Pin, HIGH);
    Serial.println("LED 2 OFF");
    
    // Start moving Motor 1 forward
    digitalWrite(motor1Pin1, HIGH);
    digitalWrite(motor1Pin2, LOW);
    Serial.println("Motor 1 moving forward");
    
    
    // Start moving Motor 2 backward
    digitalWrite(motor1Pin2, HIGH);
    digitalWrite(motor2Pin2, HIGH);
    Serial.println("Motor 2 moving backward");
    
    motorsRunning = true; // Motors are now running
    ledsOn = true; // LEDs are on
  }

  // If no motion detected, keep LEDs on if they've been turned on
  if (pirState == LOW && ledsOn) {
    Serial.println("No motion detected, but LEDs are still ON.");
    delay(40000);
  }
  
  // Motors keep running if the stop button is not pressed
  if (motorsRunning) {
    digitalWrite(motor1Pin1, HIGH);
    digitalWrite(motor1Pin2, LOW);
    digitalWrite(motor2Pin1, LOW);
    digitalWrite(motor2Pin2, HIGH);
    Serial.println("Motors are running.");
  }
}
