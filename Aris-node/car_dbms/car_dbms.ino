#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>
#include <ESP8266HTTPClient.h>
#define WLAN_SSID       "sreexerox_Ext"
#define WLAN_PASS       "987654321"
const char* ssid = "CAR";
const char* password = "12345abcd";
const String postId = "demo1";
int max_connection = 8;
String URL;
int httpCode;
String payload;
ESP8266WebServer server(80);
HTTPClient http;
IPAddress ip (10, 10, 66, 31);
IPAddress gateway (10, 10, 64, 1);
IPAddress subnet (255, 255, 248, 0);
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

  String vehicleNo = server.arg("vehicleNo");
  String nameOfOwner = server.arg("name");
  String location = server.arg("location");
  String phoneNumber = server.arg("phoneNumber");
  String typeOfAccident = server.arg("type");
  server.send( 1, "text/plain", "Response");
  Serial.println("------------------");
  Serial.println("Vehicle Number:"+vehicleNo);
  Serial.println("Owner Name    :"+nameOfOwner);
  Serial.println("Location      :"+location);
  Serial.println("Phone Number  :"+phoneNumber);
  Serial.println("Accident Type :"+typeOfAccident);
 digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
 digitalWrite(LED_BUILTIN, HIGH);

  HTTPClient http;
  http.begin("http://192.168.43.103/acc.php");
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");
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
  int httpResponceCode = http.POST("loc=" + location + "&spot=" + postId+"&vno=" + vehicleNo+"&pno=" + phoneNumber +"&typeOfAccident=" +typeOfAccident);
  Serial.print(httpResponceCode);
 
}

void loop () {
  server.handleClient();
 
}
