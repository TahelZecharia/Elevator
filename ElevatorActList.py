from ElevatorAct import ElevatorAction
from InterfaceElevatorActList import InterfaceElevatorActList

# This class implements the ElevatorActList Interface


class ElevatorActList(InterfaceElevatorActList):

    def __init__(self):
        self.__elev_list = []

    def get_list(self) -> list:
        return self.__elev_list

    def add_elev(self, elev: ElevatorAction):
        self.__elev_list.append(elev)

    def get_elev(self, index) -> ElevatorAction:
        return self.__elev_list[index]
