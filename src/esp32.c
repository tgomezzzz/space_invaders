void setup() {
  Serial.begin(115200);
  delay(1000); // give me time to bring up serial monitor
}

void loop() {
  // Potentiometer
  Serial.print(analogRead(12));
  Serial.print(",");

  // Joystick
  Serial.print(analogRead(26));
  Serial.print(",");

  // Button
  pinMode(13, INPUT_PULLUP);
  Serial.println(digitalRead(13));

  delay(20);
}
