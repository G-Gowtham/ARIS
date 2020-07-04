#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>
#include <ESP8266HTTPClient.h>
#include <String.h>
#define WLAN_SSID       "ARS"
#define WLAN_PASS       "iot@@bit"
const char* ssid = "CAR";
const char* password = "12345abcd";
int max_connection = 8;
String URL;
int httpCode;
String payload;
ESP8266WebServer server(80);
HTTPClient http;
IPAddress ip (10, 10, 66, 31);
IPAddress gateway (10, 10, 64, 1);
IPAddress subnet (255, 255, 248, 0);
String ID;
String state;
String state1;
String state2;
String state3;
String state4;
void setup() {
  Serial.begin(9600);
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
    pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
  WiFi.mode(WIFI_AP);
  Serial.println("Setup Access point");
  Serial.println("Disconnect from any other modes");
  WiFi.disconnect();
  Serial.println("stating access point with SSID" + String(ssid));
  WiFi.softAP(ssid, password, 1, false, max_connection);
  WiFi.softAPConfig(ip, gateway, subnet);
  IPAddress myIP = WiFi.softAPIP();
  Serial.println(myIP);
  server.on("/", handleroot);
  server.on("/feed", feed);
  server.begin();
}
void handleroot() {

  server.send( 1, "text/plain", "hello");
}
void feed() {

  String data1 = server.arg("ID");
  String data2 = server.arg("state");
  String data3 = server.arg("state1");
  String data4 = server.arg("state2");
  String data5 = server.arg("state3");
  String data6 = server.arg("state4");

  server.send( 1, "text/plain", "Response");
  Serial.println(data1);
  Serial.println(data2);
  Serial.println(data3);
  Serial.println(data4);
  Serial.println(data5);
  Serial.println(data6);
 digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
 digitalWrite(LED_BUILTIN, HIGH);

 
String data7="iotlab";
String data8 ="12";
String data9 ="1";
String data10 ="1,2,3,4";

  String n = data1;
  String n1 = data2;
  String n2 = data3;
  String n3 = data4;
  String n4= data5;
  String n5 = data6;
  String n6 = data7;
   String n7 = data8;
   String n8 = data9;

  String n9 = data10;
  
  
  
  HTTPClient http;
  http.begin("http://10.10.110.5/acc/car.php");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
  int httpResponceCode = http.POST("n=" + n + "&n1=" + n1+"&n2=" + n2+"&n3=" + n3+"&n4=" + n4+"&n5=" + n5+"&n6=" + n6+"&n7=" + n7+"&n8=" + n8+"&n9=" + n9);
  Serial.print("Connecting to ");
  Serial.println(WLAN_SSID);
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  
 
}

void loop () {
  server.handleClient();
 
}
