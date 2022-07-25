#include <ESP8266WiFi.h>
#include<DHT.h>
#include <FirebaseESP8266.h>
int val2;
String last_read="0";
#define sen A0
#define DHTPIN 0
#define led 1
#define WIFI_SSID "realme 6"    // replace MySSID with your WiFi network name
#define WIFI_PASSWORD "12345678"
#define FIREBASE_HOST "https://agri1-platform-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "3OIFEN0RNKrJJIe1PA2wk8GVAI2qy3HW7dm3shfb" 
FirebaseData fbdo;
FirebaseData firebaseData;
DHT dht(DHTPIN, DHT11);
float temp;
float hum;
void setup() {
  Serial.begin(115200);  // Select the same baud rate if you want to see the datas on Serial Monitor
  Serial.println("Serial communication started\n\n");            
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);                                     //try to connect with wifi
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
    Serial.println();
  Serial.print("Connected to ");
  Serial.println(WIFI_SSID);                                          //print local IP address
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  dht.begin();
  delay(1000);
  Serial.println("Program started");
}

void loop(){
     // start working...
  val2 = analogRead(sen);
  hum = dht.readHumidity();
  temp = dht.readTemperature();
   if (Firebase.setString(firebaseData, "/data", val2)) {    // On successful Write operation, function returns 1  
               Serial.println("Value Uploaded Successfully");
               Serial.print("Val = ");
               Serial.println(val2);
               Serial.println("\n");
               delay(5000);
     }

else {        
    Serial.println(firebaseData.errorReason());
  }
  if (Firebase.setString(firebaseData, "/data2", hum)) {    // On successful Write operation, function returns 1  
               Serial.println("Value Uploaded Successfully");
               Serial.print("hum, = ");
               Serial.println(hum);
               Serial.println("\n");
               delay(5000);
     }

else {        
    Serial.println(firebaseData.errorReason());
  }
  if (Firebase.setString(firebaseData, "/data3", temp)) {    // On successful Write operation, function returns 1  
               Serial.println("Value Uploaded Successfully");
               Serial.print("temp = ");
               Serial.println(temp);
               Serial.println("\n");
               delay(5000);
     }

else {        
    Serial.println(firebaseData.errorReason());
  }
   if (Firebase.getString(fbdo, "/data1")) {

      if (fbdo.dataTypeEnum() == fb_esp_rtdb_data_type_string) {
        String m =fbdo.to<String>();
       
       if(m!=last_read)
       {
            //Serial.print("STATUS ");  
            Serial.println(m);
        
            //Serial.println(last_read);
       }
       last_read=m;
     
      }

  }
    else
      Serial.println(fbdo.errorReason());
}
