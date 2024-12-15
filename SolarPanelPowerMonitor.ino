#include <Wire.h>
#include <ESP8266WiFi.h>
#include <INA219_WE.h>
#include <WiFiUdp.h>
#include <ArduinoJson.h>
#include <NTPClient.h>

#define I2C_ADDRESS 0x40
const char* ssid = "Galaxy S23 Ultra B7_94_04"; 
const char* password = "qkrtkddnr0118";  
const char* host = "192.168.160.125";
const uint16_t port = 8080;

INA219_WE ina219(I2C_ADDRESS);
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "pool.ntp.org", 60 * 60 * 9, 60000); 
WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  Wire.begin(D2, D1); 
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  if(!ina219.init()){
    Serial.println("INA219 not connected!");
  }
  
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  Serial.println("INA219 Current Sensor with solar panel");
  
  timeClient.begin(); 
}

void loop() {
  timeClient.update(); 

  float shuntVoltage_mV = 0.0;
  float loadVoltage_V = 0.0;
  float busVoltage_V = 0.0;
  float power_mW = 0.0; 
  bool ina219_overflow = false;
  
  shuntVoltage_mV = ina219.getShuntVoltage_mV();
  busVoltage_V = ina219.getBusVoltage_V();
  power_mW = ina219.getBusPower();
  loadVoltage_V  = busVoltage_V + (shuntVoltage_mV/1000);
  ina219_overflow = ina219.getOverflow();

  DynamicJsonDocument doc(256);
  doc["device_type"] = "solar_panel";
  doc["device_id"] = "SP001";
  doc["power_value"] = power_mW; // 전력 값을 JSON에 추가
  doc["timestamp"] = timeClient.getFormattedTime();

  String payload;
  serializeJson(doc, payload);

  udp.beginPacket(host, port);
  udp.print(payload);
  udp.endPacket();

  Serial.println("Data sent: " + payload);

  if(!ina219_overflow){
    Serial.println("Values OK - no overflow");
  }
  else{
    Serial.println("Overflow! Choose higher PGAIN");
  }
  
  delay(1000);
}
