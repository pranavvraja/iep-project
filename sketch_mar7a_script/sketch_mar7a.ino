// Define pins for the ultrasonic sensor
const int trigPin = 2;  // Trig pin connected to digital pin 2
const int echoPin = 3;  // Echo pin connected to digital pin 3

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  // Initialize the ultrasonic sensor pins
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  // Measure distance using the ultrasonic sensor
  long duration, distance;
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;  // Calculate distance in cm
  
  // Send distance to the laptop via serial communication
  Serial.print("Distance: ");
  Serial.println(distance);
  
  // Wait before taking the next reading
  delay(500);  // Adjust delay according to desired sensor update rate
}
