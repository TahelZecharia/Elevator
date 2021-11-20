from Ex1.ElevatorAct import ElevatorAction

# This is an interface to a list that contains ElevatorAct


class InterfaceElevatorActList:

    # This is a function that returns the ElevatorAct list
    def get_list(self) -> list:
        raise NotImplementedError

    # This is a function that receives an ElevatorAct and puts it on the list
    def add_elev(self, elev: ElevatorAction):
        raise NotImplementedError

    # This is a function that gets an index and returns the ElevatorAct in that index
    def get_elev(self, index) -> ElevatorAction:
        raise NotImplementedError
