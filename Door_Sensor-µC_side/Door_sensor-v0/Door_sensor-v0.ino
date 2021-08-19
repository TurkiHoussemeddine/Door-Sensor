#include <SoftwareSerial.h>
SoftwareSerial BT(4,6);//rx,tx
int SensorData = 7 ;

void setup() {
pinMode(8,OUTPUT);    
digitalWrite(8,HIGH); // supply 5v to IR sensor through D8
pinMode(SensorData,INPUT) ; // set D7 to input for listening
Serial.begin(9600); // for debug
BT.begin(38400);  // start BT serial @38400 bauds
BT.println("bluetooth ready");  // print something on PC side
}

void loop() {
int signl ;  
signl = digitalRead(SensorData);  // read sensor data
BT.println(signl);  // send sensor data to PC
Serial.print(signl);  // for debug
delay(100); // wait for data to reach PC
}
