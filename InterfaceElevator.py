from Ex1.Call import Call


class InterfaceElevator:

    def get_ID(self) -> int:
        raise NotImplementedError

    def get_speed(self) -> float:
        raise NotImplementedError

    def get_min_floor(self) -> int:
        raise NotImplementedError

    def get_max_floor(self) -> int:
        raise NotImplementedError

    def get_open_time(self) -> float:
        raise NotImplementedError

    def get_close_time(self) -> float:
        raise NotImplementedError

    def get_start_time(self) -> float:
        raise NotImplementedError

    def get_stop_time(self) -> float:
        raise NotImplementedError

    def get_calls_list(self) -> list:
        raise NotImplementedError

    def add_calls(self, call: Call):
        raise NotImplementedError
