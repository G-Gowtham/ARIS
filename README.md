#                                                            ARIS - Accident Rescue and Investigation System


 #                                                           Repositories info

* ARIS-model           --- 3d model of the Hardware case for our Module

* Aris-executable      --- portable Windows executable application (click aris.bat to run)

* Aris-node            --- aris node module's code

* Aris-prevention      --- aris prevention module's code 

* Aris-server          --- aris server code

* Aris-web             --- aris web application (python - flask backended)
                                                        

#                                                                      OVERVIEW OF OUR PROJECT
                                  
*	Prevention before the Accident
*	Identifying the Accident 
*	Rescue of the Accident 

##                                                                            Prevention before the Accident

*	To Prevent The Accidents And To Identify The Accident Prone Zones , School Zones , Indicating Alcohol Consumption , 
Hairpin Bends.

*	It Will Display In LCD Monitor Of The Car.

*   We are identifying the accident prone zones using the previous accidents data so that our module could be placed there to avoid furthur accidents.

##                                                                       Identifying the Accident

*	Crashing Of Cars

*	Flipping Of Cars

*	Fire Accident

*	If The Accident Occurs Either By Crashing Of Car Or Fire Accident . In Which We Have Already Used The Existing System (Air Bag Concept And Fire Detector)And Enhanced It, Which Is Connected To The Module To Fetch The Data . 

*	For Flipping Of Car We Have Inserted Gyroscope Sensor To Find The Angle Of Deviation In Which It Exceed 45 To 60 Degree, In Such Case The Car Will Be Flipped All These Information Will Send To Server Side.

##                                                                       Rescue Of The Accident
                                                                       
THERE ARE TWO CASES 

 If Accident Near The Receiver 
 
*	 The receiver module  can be  placed in any highest place , here we have used lamppost ,which can be seen everywhere in the roadways.  The receiver module is kept 0.5 to 1 km wide in range (depends upon area). 

*	When accident occurs near the receiver module , the module in the car(transmitter) sends the data to the module in receiver and that sends to the cloud .

*	 The data from the cloud, sends to the rescue system and family by alerting with the message and GPS location .

 If Accident Far Away From The Receiver
 
*	In case , if the receiver is far away from the car, the data hops from  the car to the  neighbouring car(i.e. The module is mandatory in all cars , which operates without the internet) which is near to the receiver , and the process continues till it reaches the receiver .

*	The data from the cloud , sends to the rescue system and family by alerting with the message . 





#                                                                          SIGNIFICANT FEATURES

*	The module in the receiver can be wired or wireless with GPS location .

*	The video of the accident is captured and  it is cropped to a 3 min video for future investigation(placing of camera is optional)

*	In urban areas we shall use wired communication to transfer data from receiver to cloud due to its low latency . So data can be transfer in high rate of speed .

*	In rural areas we shall use wireless communication 

*	In case of multiple accident , we can get data from at least of 10 vehicle at a time from same car . 
This Will Lead To Decrease In Death Rate Both In Day And Night Time As Well.  Well , We Have Designed This To Prevent , Point Out And  Protect .
