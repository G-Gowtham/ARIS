// if (y >= 40 && y <= 70 || y >= 110 && y <= 130 ||c==0 )
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <Wire.h>
const int c = D3;
int D = 0;
const int MPU_addr = 0x68;
int16_t axis_X, axis_Y, axis_Z;
int minVal = 265;
int maxVal = 402;
double x;
double y;
double z;
String data;
const String vehicleNo = "TN 98 AB 9988";
const String nameOfOwner = "Andrew";
const String location = "10.975731,77.498113";
const String phoneNumber = "423256788765";
const String typeFlip = "FLIPPED";
const String typeCrash = "CRASHED";
const char *ssid = "CAR";
const char *password = "12345abcd";
String host = "http://10.10.66.31/feed?";

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

  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);
}

void readdata()
{
  D = digitalRead(c);
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr, 14, true);
  axis_X = Wire.read() << 8 | Wire.read();
  axis_Y = Wire.read() << 8 | Wire.read();
  axis_Z = Wire.read() << 8 | Wire.read();
  int xAng = map(axis_X, minVal, maxVal, -90, 90);
  int yAng = map(axis_Y, minVal, maxVal, -90, 90);
  int zAng = map(axis_Z, minVal, maxVal, -90, 90);
  x = RAD_TO_DEG * (atan2(-yAng, -zAng) + PI);
  y = RAD_TO_DEG * (atan2(-xAng, -zAng) + PI);
  z = RAD_TO_DEG * (atan2(-yAng, -xAng) + PI);

  Serial.print("Angle of inclination in Z axis= ");
  Serial.print(z);
  Serial.println((char)176);
  Serial.println("-------------------------------------------");
  delay(1000);

  Serial.println(D);

  if (z >= 20 && z <= 110 || z >= 250 && z <= 275 || D == 0)
  {
    digitalWrite(LED_BUILTIN, LOW);

    data = "vehicleNo=";
    data += String(vehicleNo);

    data += "&name=";
    data += String(nameOfOwner);

    data += "&location=";
    data += String(location);

    data += "&phoneNumber=";
    data += String(phoneNumber);

    data += "&type=";
    data += String(typeFlip);
    http.begin(host);
    http.addHeader("content-type", "application/x-www-form-urlencoded");
    http.POST(data);
    http.writeToStream(&Serial);
    http.end();
    Serial.println("data stream: " + data);
  }
  if (D == 0)
  {
    digitalWrite(LED_BUILTIN, LOW);
    data = "vehicleNo=";
    data += String(vehicleNo);

    data += "&name=";
    data += String(nameOfOwner);

    data += "&location=";
    data += String(location);

    data += "&phoneNumber=";
    data += String(phoneNumber);

    data += "&type=";
    data += String(typeCrash);

    http.begin(host);
    http.addHeader("content-type", "application/x-www-form-urlencoded");
    http.POST(data);
    http.writeToStream(&Serial);
    http.end();
    Serial.println("data stream: " + data);
  }

  else
  {
    digitalWrite(LED_BUILTIN, HIGH);
  }
}

void loop()
{
  readdata();
}
