import json
# from Elevator import Elevator
# from InterfaceBuilding import InterfaceBuilding
from elevTry import Elevator

class Building:  # להוסיף אינטרפייס

    def __init__(self):
        self.__minFloor: int = 0
        self.__maxFloor: int = 0
        self.__elevators: dict = {}

    def loadJson(self, file_name):
        try:
            with open(file_name, "r+") as f:
                newElevators = {}
                myDict = json.load(f)
                self.__minFloor = myDict["_minFloor"]
                self.__maxFloor = myDict["_maxFloor"]
                elevList = myDict["_elevators"]  # list of all the elevators
                for x in elevList:
                    e = Elevator(**x)
                    newElevators[e.getID()] = e  # placing the elevators on a dictionary
                self.__elevators = newElevators
        except IOError as e:
            print(e)

    def getMinFloor(self) -> int:
        return self.__minFloor

    def getMaxFloor(self) -> int:
        return self.__maxFloor

    def getNumberOfElevators(self) -> int:
        return len(self.__elevators)

    def getElevatorsDict(self) -> int:
        return self.__elevators

    def getElevator(self, idOfElevator: int) -> Elevator:
        return self.__elevators.get(idOfElevator)

    def __str__(self) -> str:
        return f"min floor:{self.__minFloor}, max floor:{self.__maxFloor}," \
               f" num of elevators:{self.getNumberOfElevators()}, elevators:{self.__elevators.__repr__()}"


# if __name__ == '__main__':
#     b2: Building = Building()
#     print(b2)
#     b2.loadJson("B2.json")
#     print(b2)
