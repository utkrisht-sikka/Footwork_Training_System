const int states1=A0;
const int states2=A1;
const int states3=A2;
const int states4=A3;
const int states5=A4;
const int states6=A5;
int state1;
int state2;
int state3;
int state4;
int state5;
int state6;
const int d=12;

char data;

const int t=500;


void setup(){
  Serial.begin(9600);
  pinMode(states1,INPUT);
  pinMode(states2,INPUT);
  pinMode(states3,INPUT);
  pinMode(states4,INPUT);
  pinMode(states5,INPUT);
  pinMode(states6,INPUT);
}
void loop(){
 while (Serial.available()){
  data = Serial.read();
  }
 if (data=='1'){
  delay(t);
Serial.flush();
  set1();
  
}
else if (data=='2'){
  delay(t);
Serial.flush();
  set2();
}
else if (data=='3'){
  delay(t);
Serial.flush();
  set3();
}
data='0';//if inputing from serial monitor,remove this statement
}

int set1(){
 state5=analogRead(states5);
while (state5>d){
 
 Serial.println(String(state5)+';'+"state5"); 
 delay(t);
Serial.flush();
state5=analogRead(states5);
}
Serial.println("correct");
delay(t);
Serial.flush();
state6=analogRead(states6);
while (state6>d){
 
 Serial.println(String(state6)+';'+"state6"); 
 delay(t);
Serial.flush();
state6=analogRead(states6);
}
Serial.println("correct");
delay(t);
Serial.flush();
state3=analogRead(states3);
while (state3>d){
 Serial.println(String(state3)+';'+"state3"); 
 delay(t);
Serial.flush();
state3=analogRead(states3);
}
Serial.println("correct");
delay(t);
Serial.flush();
state5=analogRead(states5);
while (state5>d){
  Serial.println(String(state5)+';'+"state5"); 
 delay(t);
Serial.flush();
state5=analogRead(states5);
}
Serial.println("correct");
delay(t);
Serial.flush();
return 1;
}

int set2(){
 state2=analogRead(states2);
 
while (state2>d){
 Serial.println(String(state2)+';'+"state2"); 
 delay(t);
Serial.flush();
  state2=analogRead(states2);
}
Serial.println("correct");
delay(t);
Serial.flush();
state1=analogRead(states1);
while (state1>d){
  Serial.println(String(state1)+';'+"state1"); 
 delay(t);
Serial.flush();
  state1=analogRead(states1);
}
Serial.println("correct");
delay(t);
Serial.flush();
state5=analogRead(states5);
while (state5>d){
  Serial.println(String(state5)+';'+"state5"); 
 delay(t);
Serial.flush();
  state5=analogRead(states5);
}
Serial.println("correct");
delay(t);
Serial.flush();
state4=analogRead(states4);
while (state4>d){
  Serial.println(String(state4)+';'+"state4"); 
 delay(t);
Serial.flush();
  state4=analogRead(states4);
}
Serial.println("correct");
delay(t);
Serial.flush();
state3=analogRead(states3);
while (state3>d){
  Serial.println(String(state3)+';'+"state3"); 
 delay(t);
Serial.flush();
  state3=analogRead(states3);
}
Serial.println("correct");
delay(t);
Serial.flush();
state2=analogRead(states2);
while (state2>d){
  Serial.println(String(state2)+';'+"state2"); 
 delay(t);
Serial.flush();
   state2=analogRead(states2);
}
Serial.println("correct");
delay(t);
Serial.flush();
state5=analogRead(states5);
while (state5>d){
  Serial.println(String(state5)+';'+"state5"); 
 delay(t);
Serial.flush();
   state5=analogRead(states5);
}
Serial.println("correct");
delay(t);
Serial.flush();
state6=analogRead(states6);
while (state6>d){
  Serial.println(String(state6)+';'+"state6"); 
 delay(t);
Serial.flush();
   state6=analogRead(states6);
}
Serial.println("correct");
delay(t);
Serial.flush();
return 1;
}


int set3(){
 
 state3=analogRead(states3);
 
while (state3>d){
 Serial.println(String(state3)+';'+"state3"); 
 delay(t);
Serial.flush();
   state3=analogRead(states3);
}
Serial.println("correct");
delay(t);
Serial.flush();
state5=analogRead(states5);
while (state5>d){
  Serial.println(String(state5)+';'+"state5"); 
 delay(t);
Serial.flush();
   state5=analogRead(states5);
}
Serial.println("correct");
delay(t);
Serial.flush();
state4=analogRead(states4);
while (state4>d){
  Serial.println(String(state4)+';'+"state4"); 
 delay(t);
Serial.flush();
   state4=analogRead(states4);
}
Serial.println("correct");
delay(t);
Serial.flush();
state6=analogRead(states6);
while (state6>d){
  Serial.println(String(state6)+';'+"state6"); 
 delay(t);
Serial.flush();
   state6=analogRead(states6);
}
Serial.println("correct");
delay(t);
Serial.flush();
return 1;
}
