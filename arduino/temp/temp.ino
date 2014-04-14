void setup() {            //This function gets called when the Arduino starts
  Serial.begin(9600);   //This code sets up the Serial port at 9600 baud rate
}


double Thermister(int RawADC) {  //Function to perform the fancy math of the Steinhart-Hart equation
  return RawADC;
/* double Temp;
 Temp = RawADC/1023*5;
 Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
 Temp = Temp - 273.15;              // Convert Kelvin to Celsius
 // Temp = (Temp * 9.0)/ 5.0 + 32.0; // Celsius to Fahrenheit - comment out this line if you need Celsius
 return Temp;*/
}
 
void loop() {             //This function loops while the arduino is powered
  int val;                //Create an integer variable
  int heartrate;
  val=analogRead(0);      //Read the analog port 0 and store the value in val
  heartrate=analogRead(1); 
  Serial.print(val); 
 Serial.print("------");  
  Serial.println(heartrate);    //Print the value to the serial port
  delay(100);            //Wait one second before we do it again
}

