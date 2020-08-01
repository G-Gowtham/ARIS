#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>
#include <ESP8266HTTPClient.h>
const char* ssid = "CAR";
const char* password = "12345abcd";
int max_connection = 8;
String URL;
int httpCode;
String payload;
ESP8266WebServer server(80);
HTTPClient http;
IPAddress ip (10, 10, 66, 32;
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

  String indiactorSignal = server.arg("indicatorSignal");
  server.send( 1, "text/plain", "Response");
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
  }.
  Serial.println();
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  int httpResponceCode = http.POST("indicator="+indicatorSignal);
  Serial.print(httpResponceCode);
 
}

void loop () {
  server.handleClient();
 
}
