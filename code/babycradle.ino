#define sound 2
#define m1 4
const int rain = A1;
#include "DHT.h"
#define DHTPIN 3
#define DHTTYPE DHT11   // DHT 11

DHT dht(DHTPIN, DHTTYPE);
float temp_val;
float hum_val;


int s1;
void setup() {
  // put your setup code here, to run once:
  pinMode(sound,INPUT);
  pinMode(m1,OUTPUT);
  dht.begin();
  digitalWrite(m1,HIGH);
 
  Serial.begin(9600);
  
}

void loop() {
  // put your main code here, to run repeatedly:

  s1=digitalRead(sound);
  Serial.print(s1);
  if (s1==0)
  {
    
    digitalWrite(m1,LOW);
//    
    delay(5000);
    digitalWrite(m1,HIGH);
    Serial.print("Sound #");
    
  }

  temp_val = dht.readTemperature(); /* Read Temperature */
 
  Serial.print("Temp : ");
  Serial.print(temp_val);
  delay(10);
  Serial.print("#");
  hum_val=dht.readHumidity();
  Serial.print(" Hum : ");
  Serial.println(hum_val);

  float rn = analogRead(rain);

  Serial.println(rn);
  
  
  delay(500);

}
