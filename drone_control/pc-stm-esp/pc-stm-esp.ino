char SSID[]="sesrv";
char PASSWD[]="0434043402320232";
void connect()
{
  Serial1.println("AT+RST");
  delay(500);
  Serial1.println("AT+CWMODE=1");
  delay(500);
  Serial1.print("AT+CWJAP=\"");
  Serial1.print(SSID);
  Serial1.print("\",\"");
  Serial1.print(PASSWD);
  Serial1.println("\"");
  delay(6000);
  Serial1.println("AT+CIFSR");
  delay(500);
  Serial1.println("AT+CIPMUX=1");
  delay(500);
  Serial1.println("AT+CIPSERVER=1,80");
  digitalWrite(PC13,LOW); // turn led on
  delay(500);
  
}
void setup()
{
  Serial1.begin(115200);  // esp
  Serial.begin(115200);     // usb
  while(!Serial1)
  {}
  pinMode(PC13,OUTPUT);
  digitalWrite(PC13,HIGH);
  delay(1000);
  Serial.println("START");
  connect();
  Serial.println("OK");
}
void ON()
{
  digitalWrite(PC13,LOW);
}
void OFF()
{
  digitalWrite(PC13,HIGH);
}
void loop()
{
  
  if(Serial.available())
  {
    Serial1.write(Serial.read());
  }
  
  if(Serial1.available())
  {
    Serial.write(Serial1.read());
  }
}
