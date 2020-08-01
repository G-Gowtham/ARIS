#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
const int c = D3;
int D = 0;
const char *ssid = "CAR";
const char *password = "12345abcd";
String host = "http://10.10.66.32/feed?";
const String indicator = "Hair Pin";
WiFiClient client;
HTTPClient http;

IPAddress ip(10, 10, 66, 32);
IPAddress gateway(10, 10, 64, 1);
IPAddress subnet(255, 255, 248, 0);

void setup()
{

  Serial.begin(115200);
  pinMode(c, INPUT);
  ESP.eraseConfig();
  WiFi.persistent(false);
  Serial.println("SET ESP IN STA MODE");
  WiFi.mode(WIFI_STA);
  Serial.println("- connecting to wifi");
  WiFi.config(ip, gateway, subnet);
  WiFi.begin(ssid, password);
  Serial.println(".");
  Serial.println("- wifi connected");
  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void readdata()
{
  
    digitalWrite(LED_BUILTIN, LOW);
    data = "indicatorSignal=";
    data += indicator;
    http.begin(host);
    http.addHeader("content-type", "application/x-www-form-urlencoded");
    http.POST(data);
    http.writeToStream(&Serial);
    http.end();
    Serial.println("data stream: " + data);
  }

void loop()
{
  readdata();
}
