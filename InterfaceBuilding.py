from Elevator import Elevator

# This is an interface to the building


class InterfaceBuilding:

    # This function loads from a Jason file into the building and into a dictionary of elevators
    def loadJson(self, file_name):
        raise NotImplementedError

    # This function returns the min floor in the building
    def getMinFloor(self) -> int:
        raise NotImplementedError

    # This function returns the max floor in the building
    def getMaxFloor(self) -> int:
        raise NotImplementedError

    # This function returns the number of elevators in the building
    def getNumberOfElevators(self) -> int:
        raise NotImplementedError

    # This function get an index of elevator and returns the desired elevator
    def getElevator(self, idOfElevator: int) -> Elevator:
        raise NotImplementedError

