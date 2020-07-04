#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <SoftwareSerial.h>
#include <ESP8266HTTPClient.h>
#include <String.h>
#define WLAN_SSID       "ARS"
#define WLAN_PASS       "iot@@bit"
const int buttonPin = D1;
int buttonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(buttonPin, OUTPUT);
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
  buttonState = digitalRead(buttonPin);
  Serial.println(buttonState);
  if (buttonState == 1)

  {
    Serial.println("Women safety");
    String n = "~";
    String n1 = "~";
    String n2 = "~";
    String  n3 = "~";
    String  n4 = "~";
    String  n5 = " SOS ";
    String  n6 = "Iotlab";
    String  n7 = "1";
    String  n8 = "2";
    String  n9 = "1,2,3,4";
    HTTPClient http;
    http.begin("http://10.10.110.5/acc/car.php");
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    int httpResponceCode = http.POST("n=" + n + "&n1=" + n1 + "&n2=" + n2 + "&n3=" + n3 + "&n4=" + n4 + "&n5=" + n5 + "&n6=" + n6 + "&n7=" + n7 + "&n8=" + n8 + "&n9=" + n9);
  }
  delay(200);
}
