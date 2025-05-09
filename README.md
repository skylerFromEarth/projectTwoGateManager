gateManager1.py is my PyQT GUI.  
main.py is the launch point for the application and ties things together.
logicGateManager.py is where I tie in the code from raceGateManager.py and the buttons from the GUI
raceGateManager.py sets up and organizes the event of a race happening

GateManager is an application designed to organize and record data for race track operators to help make the gate loading process
more efficient.  The user will be prompted to pick a date from a calendar dropdown.  Then choose a track.  Then enter in the race number.
Then enter in the number of horses in the race.  When horses begin entering the starting gate the user hits the button named
"Entering Starting Gate" then timer begins.  Once all horses are in the starting gate, the gates open and that is when you push Race Off, and the timer ends.  
Then this data is saved in dataGateManager.csv in the format of Date, Track, Race Number, Number of Horses, Beginning Load Time, Race Off Ending Load Time, Duration of Load, Average Time to Load Each Horse
