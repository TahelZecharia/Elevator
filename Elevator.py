from Ex1.Call import Call


class Elevator:

    def __init__(self, _id: int, _speed: float, _minFloor: int,
                 _maxFloor: int, _closeTime: float, _openTime: float,
                 _startTime: float, _stopTime: float):
        self.__id: int = _id
        self.__speed: float = _speed
        self.__min_floor: int = _minFloor
        self.__max_floor: int = _maxFloor
        self.__close_time: float = _closeTime
        self.__open_time: float = _openTime
        self.__start_time: float = _startTime
        self.__stop_time: float = _stopTime
        self.__calls_list: list = []

    def get_ID(self) -> int:
        return self.__id

    def get_speed(self) -> float:
        return self.__speed

    def get_min_floor(self) -> int:
        return self.__min_floor

    def get_max_floor(self) -> int:
        return self.__max_floor

    def get_open_time(self) -> float:
        return self.__open_time

    def get_close_time(self) -> float:
        return self.__close_time

    def get_start_time(self) -> float:
        return self.__start_time

    def get_stop_time(self) -> float:
        return self.__stop_time

    def get_calls_list(self) -> list:
        return self.__calls_list

    def add_calls(self, call: Call):
        return self.__calls_list.append(call)

    def __str__(self):
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s"\
               % (self.__id, self.__speed, self.__min_floor, self.__max_floor, self.get_close_time(),
                  self.get_open_time(), self.get_start_time(), self.get_stop_time())

    def __repr__(self):
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s"\
               % (self.__id, self.__speed, self.__min_floor, self.__max_floor, self.get_close_time(),
                  self.get_open_time(), self.get_start_time(), self.get_stop_time())

