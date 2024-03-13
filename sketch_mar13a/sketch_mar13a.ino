#define trigPin1 6  // Trigger pin for sensor 1
#define echoPin1 5   // Echo pin for sensor 1
#define trigPin2 11 // Trigger pin for sensor 2
#define echoPin2 12  // Echo pin for sensor 2

long duration1, duration2; // Store pulse durations
int distance1, distance2; // Calculated distances

void setup() {
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  Serial.begin(9600); // Establish serial communication
}

void loop() {
  // Read distance from sensor 1
  distance1 = readDistance(trigPin1, echoPin1);
  // Read distance from sensor 2
  distance2 = readDistance(trigPin2, echoPin2);

  // Send distance data to Python script via serial communication
  Serial.print("distance1:");
  Serial.println(distance1);
  Serial.print("distance2:");
  Serial.println(distance2);

  delay(1000); // Delay between readings
}

long readDistance(int trigPin, int echoPin) {
  // Function to measure distance using HC-SR04 sensor
  // You can find existing code for this online (example provided below)
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration1 = pulseIn(echoPin, HIGH);
  return duration1 * 0.034 / 2;  // Convert pulse duration to distance in cm
}
