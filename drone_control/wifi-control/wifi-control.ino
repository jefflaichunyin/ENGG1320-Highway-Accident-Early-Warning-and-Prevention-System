
char SSID[]="sesrv";
char PASSWD[]="0434043402320232";
int state=0;
void connect()
{
  //Serial1.println("AT+RST");
  //delay(3000);
  Serial1.println("AT+CWMODE=1");
  delay(500);
  Serial1.print("AT+CWJAP=\"");
  Serial1.print(SSID);
  Serial1.print("\",\"");
  Serial1.print(PASSWD);
  Serial1.println("\"");
  delay(10000);
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
  while(!Serial1)
  {}
  pinMode(PC13,OUTPUT);
  pinMode(PA15, OUTPUT);
  digitalWrite(PC13,HIGH);
  digitalWrite(PA15,LOW);
  delay(1000);
  connect();

}
void changeState()
{
  state = !state;
  digitalWrite(PA15, state);
}
void ON()
{
  Timer1.setMode(TIMER_CH1, TIMER_OUTPUTCOMPARE);
  Timer1.setPeriod(500000);
  Timer1.attachInterrupt(TIMER_CH1, changeState);
}
void OFF()
{
  digitalWrite(PA15,LOW);
  Timer1.detachInterrupt(TIMER_CH1);
}
void loop()
{
  if(Serial1.available())
  {
    //Serial.write(Serial1.read());
    if(Serial1.find("GET /"))
    {
      String command;
      command = Serial1.readStringUntil(' ');
      if(command=="on")
        ON();
      if(command=="off")
        OFF();
    }
  }
}
