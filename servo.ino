#include <Servo.h>

Servo servo_x;

int angle_x = 0;

void setup() 
{
  Serial.begin(9600);
  servo_x.attach(9);
}

void loop() 
{
  if (Serial.available()) 
  {
    angle_x = Serial.parseInt();
    delay(500);
    servo_x.write(angle_x);
    delay(500);
    Serial.println(angle_x);
    delay(15);
  }
}
