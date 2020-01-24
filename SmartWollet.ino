void setup() {
Serial.begin(9600); // set the baud rate
Serial.println("Ready"); // print "Ready" once
pinMode(A0,INPUT_PULLUP);
pinMode(LED_BUILTIN, OUTPUT);
}


int value=210;
int Security=0;
unsigned int zapaska=0;
unsigned int this_time=0;
void loop() {
  String prekol;
if(Serial.available()){ // only send data back if data has been sent
prekol=Serial.readString();

  if(prekol=="2")value=80;
  else if(prekol=="3")value=100;
  else if(prekol=="4")value=120;
  else if(prekol=="5")value=140;
  else if(prekol=="6")value=160;
  else if(prekol=="7")value=190;
  else if(prekol=="8")value=210;
  else if(prekol=="9")value=230;
  else if(prekol=="10")value=255;
  
if(prekol=="1") analogWrite(5,value);
else if(prekol=="0")analogWrite(5,0);

if(prekol=="S"){Security=1; zapaska=0;}
else if(prekol=="N"){ Security=0;analogWrite(5,0);}


if(Security==1){
  if(prekol=="E"){
    Serial.println(zapaska);
    zapaska=0;
    this_time=millis();
    
  }
}

}

if(Security==1){
  zapaska++;
  if(zapaska>100)analogWrite(5,230);
}

//Serial.println(30);
delay(100);
  //Serial.print("ac"+String(analogRead(A0));

  
}
