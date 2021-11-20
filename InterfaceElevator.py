from Ex1.Call import Call
# this is interface to elevator


class InterfaceElevator:

    # This function returns the ID of the elevator
    def get_ID(self) -> int:
        raise NotImplementedError

    # This function returns the speed of the elevator
    def get_speed(self) -> float:
        raise NotImplementedError

    # This function returns the min floor of the elevator
    def get_min_floor(self) -> int:
        raise NotImplementedError

    # This function returns the max floor of the elevator
    def get_max_floor(self) -> int:
        raise NotImplementedError

    # This function returns the time that take the elevator to open the doors
    def get_open_time(self) -> float:
        raise NotImplementedError

    # This function returns the time that take the elevator to close the doors
    def get_close_time(self) -> float:
        raise NotImplementedError

    # This function returns the time that take the elevator to start move
    def get_start_time(self) -> float:
        raise NotImplementedError

    # This function returns the time that take the elevator to stop move
    def get_stop_time(self) -> float:
        raise NotImplementedError

    # This function returns the time list of the call that elevator need to do
    def get_calls_list(self) -> list:
        raise NotImplementedError

    # This function get a call ans add it to the calls the elevator need to do
    def add_calls(self, call: Call):
        raise NotImplementedError
