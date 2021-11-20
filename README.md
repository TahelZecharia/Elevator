# Elevator
In this project I implemented a program that gets a Jason file containing a building with elevators inside, and a csv file of calls, and returns a csv file of calls with the optimal placement for each call so that the average waiting time of all calls is as short as possible.
In this program I implemented the departments:
## Building:
Contains a function that reads from the Jason file. To it I claimed the construction given in the Jason file
## Elevator:
To it I loaded the elevators given inside the building's Gyson file.
Calls:
To it I uploaded every call from the csv file
CallsList:
Contains a list of all received calls, and implements a funk of reading from a csv file, and writing a csv file.
To it I uploaded all the readings received in the csv file
ElevatorAct:
A class that simulates an elevator in action.
ElevatorActList:
List of ElevatorAct lifts
Simulator:
There is the simulator that operates the elevator of the elevAct type and there is the cost function that receives a call and an elevator and simulates a situation where the reading is in the elevator and finally returns the time of effect of the reading on the same elevator.
My algorithm:
Given a list of readings, we will go through all the readings and check with the help of the funk cost how much the reading "costs" with the help of an image of the income of the reading to the reading list of that elevator. The function simulates the effect of the same reading on all the readings in the elevator, taking into account the location of the elevator and the direction of the readings in the elevator.

All departments have an interface where it is explained about each department and what it does, and the functions it has and what they do.
