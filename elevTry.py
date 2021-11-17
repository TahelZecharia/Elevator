from Ex1.callTry import Call


class Elevator:  # להוסיף אינטרפייס

    def __init__(self, _id: int, _speed: float, _minFloor: int,
                 _maxFloor: int, _closeTime: float, _openTime: float,
                 _startTime: float, _stopTime: float):
        self.__id: int = _id
        self.__speed: float = _speed
        self.__minFloor: int = _minFloor
        self.__maxFloor: int = _maxFloor
        self.__closeTime: float = _closeTime
        self.__openTime: float = _openTime
        self.__startTime: float = _startTime
        self.__stopTime: float = _stopTime
        self.__callsList: list = []

    def getID(self) -> int:
        return self.__id

    def getSpeed(self) -> float:
        return self.__speed

    def getMinFloor(self) -> int:
        return self.__minFloor

    def getMaxFloor(self) -> int:
        return self.__maxFloor

    def getOpenTime(self) -> float:
        return self.__openTime

    def getCloseTime(self) -> float:
        return self.__closeTime

    def getStartTime(self) -> float:
        return self.__startTime

    def getStopTime(self) -> float:
        return self.__stopTime

    def getCallsListOfElevator(self) -> list:
        return self.__callsList

    def addCallsListOfElevator(self, call: Call):
        return self.__callsList.append(call)

    def __str__(self):
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s"\
               % (self.__id, self.__speed, self.__minFloor, self.__maxFloor, self.getCloseTime(),
                  self.getOpenTime(), self.getStartTime(), self.getStopTime())

    def __repr__(self):
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s"\
               % (self.__id, self.__speed, self.__minFloor, self.__maxFloor, self.getCloseTime(),
                  self.getOpenTime(), self.getStartTime(), self.getStopTime())


# if __name__ == '__main__':

    # "_id": 0,
    # "_speed": 1.0,
    # "_minFloor": -2,
    # "_maxFloor": 10,
    # "_closeTime": 2.0,
    # "_openTime": 2.0,
    # "_startTime": 3.0,
    # "_stopTime": 3.0
    # ele: Elevator = Elevator(0,1.0,-2,4,5,6,7,8)
    # ele1: Elevator = Elevator(1, 1.0, -2,3,4,5,6,7)
    #
    # test:Dict[int,Elevator] = dict()
    # test.update({ele1.getID(): ele1})
    #
    # test.update({ele.getID(): ele})
    # print(test)
    # print(ele.getID() , ele.getSpeed(),ele.getMinFloor())
    # print(ele1.getID() , ele1.getSpeed(),ele1.getMinFloor())


    # e = {
    #     "_minFloor": -2,
    #     "_maxFloor": 10,
    #     "_elevators": [
    #         {
    #             "_id": 0,
    #             "_speed": 1.0,
    #             "_minFloor": -2,
    #             "_maxFloor": 10,
    #             "_closeTime": 2.0,
    #             "_openTime": 2.0,
    #             "_startTime": 3.0,
    #             "_stopTime": 3.0
    #         },
    #         {
    #             "_id": 1,
    #             "_speed": 2.0,
    #             "_minFloor": -2,
    #             "_maxFloor": 10,
    #             "_closeTime": 2.0,
    #             "_openTime": 2.0,
    #             "_startTime": 3.0,
    #             "_stopTime": 3.0
    #         }
    #     ],}
    # print(type(e))