from Elevator import Elevator


class InterfaceBuilding:

    def getMinFloor(self) -> int:
        raise NotImplementedError

    def getMaxFloor(self) -> int:
        raise NotImplementedError

    def getNumberOfElevators(self) -> int:
        raise NotImplementedError

    def getElevator(self, idOfElevator: int) -> Elevator:
        raise NotImplementedError


