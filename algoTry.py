import copy
from elevTry import Elevator
from callListTry import CallsList
from buildTry import Building
import copy
from Ex1 import buildTry
from callTry import Call
from elevTry import Elevator
from elevActTry import ElevatorAction
if __name__ == '__main__':

    # 1) load call list
    # print('Enter your Calls:')
    # call = input()
    cl = CallsList()
    # cl.loadCSV(call)
    cl.loadCSV("output.csv")

    # 2) load building
    # print('Enter your build:')
    # build_input = input()
    build: Building = Building()
    # build.loadJson(build_input)
    build.loadJson("B2.json")

    def cost(self, elev: Elevator, call: Call) -> float:
        el1: Elevator = copy.deepcopy(elev)
        el2: Elevator = copy.deepcopy(elev)
        el2.getCallsListOfElevator().append(call)


    # for call in cl.getCalls():
    #     #first call
    #     print(call.getTime())
    #     #for key,ele in build.getElevators().items():
    #     for ele in build.getElevators().values():
    #         #all elevetor
    #         ele:Elevator = ele


            #print(ele.getStopTime())
            #
    # print(build.getMinFloor())
    # print(cl.getCall(1).getSrc())

    # def __init__(self, _id: int, _speed: float, _minFloor: int,
    #              _maxFloor: int, _closeTime: float, _openTime: float,
    #              _startTime: float, _stopTime: float):


    # ele = Elevator(1,1.5,-1,100,0.5,1.5,0.5,1.5)
    # print(ele)