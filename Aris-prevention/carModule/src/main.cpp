// Import required libraries
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <FS.h>
String obstacle = "Drive peacefully";

const char* ssid = "CAR";
const char* password = "12345abcd";


const int ledPin = 2;
// Stores LED state
String ledState;

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);
IPAddress ip (10, 10, 66, 32);
IPAddress gateway (10, 10, 64, 1);
IPAddress subnet (255, 255, 248, 0);
String getObstacle(){
  return String(obstacle);
}
// Replaces placeholder with LED state value
String processor(const String& var){
if (var == "Drive"){
 return getObstacle();
}
 }


 
void setup(){
  // Serial port for debugging purposes
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);
  // Initialize SPIFFS
  if(!SPIFFS.begin()){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  }
WiFi.mode(WIFI_AP);
  Serial.println("Setup Access point");
  Serial.println("Disconnect from any other modes");
  WiFi.disconnect();
  Serial.println("stating access point with SSID" + String(ssid));
  WiFi.softAP(ssid, password, 1, false, 10);
  WiFi.softAPConfig(ip, gateway, subnet);
  IPAddress myIP = WiFi.softAPIP();
  Serial.println(myIP);

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/index.html", String(), false, processor);
  });
  
  // Route to load style.css file
  server.on("/style.css", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/style.css", "text/css");
  });
server.on("/getObstacle", HTTP_GET, [](AsyncWebServerRequest *request){
  request->send_P(200, "text/plain", getObstacle().c_str());
});
  server.on("/speedBreaker", HTTP_GET, [](AsyncWebServerRequest *request){
    obstacle = "Speed Breaker";
      request->send_P(200, "text/plain", getObstacle().c_str());

  });
  
  server.on("/Speedlimit", HTTP_GET, [](AsyncWebServerRequest *request){
    obstacle = "Speedlimit@40";
      request->send_P(200, "text/plain", getObstacle().c_str());

  });
  
  server.on("/harpinBend", HTTP_GET, [](AsyncWebServerRequest *request){
    obstacle = "Hairpin Bend";
      request->send_P(200, "text/plain", getObstacle().c_str());

  });
  server.on("/noLimit",HTTP_GET,[](AsyncWebServerRequest *request){
    obstacle = "No Limit";
      request->send_P(200, "text/plain", getObstacle().c_str());

  });
server.on("/peaceDrive",HTTP_GET,[](AsyncWebServerRequest *request){
    obstacle = "Drive peacefully";
      request->send_P(200, "text/plain", getObstacle().c_str());

  });
  // Start server
  server.begin();
}
 
void loop(){
  
}