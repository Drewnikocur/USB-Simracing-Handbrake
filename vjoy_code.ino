
const int potPin = 4;

void setup() {

  Serial.begin(115200);
  

  analogReadResolution(12);
  

  analogSetAttenuation(ADC_11db);
}

void loop() {

  int rawValue = analogRead(potPin);
  

  float voltage = rawValue * (3.3 / 4095.0);
  

  Serial.print("Surowa wartosc: ");
  Serial.print(rawValue);
  Serial.print(" | Napiecie: ");
  Serial.print(voltage, 2); 
  Serial.println(" V");
  

  delay(150);
}
