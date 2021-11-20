# Interface to call

class InterfaceCall:

    # This function returns the time the call was received
    def get_time(self) -> float:
        raise NotImplementedError

    # This function returns the type of the call (Up/Down)
    def get_type(self) -> str:
        raise NotImplementedError

    # This function returns the src of the call
    def get_src(self) -> int:
        raise NotImplementedError

    # This function returns if the call got to src
    def get_got_to_src(self) -> bool:
        raise NotImplementedError

    # This function set the if the call got to src
    def set_got_to_src(self):
        raise NotImplementedError

    # This function returns the dest of the call
    def get_dest(self) -> int:
        raise NotImplementedError

    # This function returns if the call got to dest
    def get_got_to_dest(self) -> bool:
        raise NotImplementedError

    # This function set the if the call got to dest
    def set_got_to_dest(self):
        raise NotImplementedError

    # This function returns the time the call got to dest
    def get_got_dest_time(self) -> float:
        raise NotImplementedError

    # This function set the time the call got to dest
    def set_got_dest_time(self, got_dest_time):
        raise NotImplementedError

    # This function set the index of the elevator the call was allocated to
    def set_allocated_to(self, elev: int):
        raise NotImplementedError

    # This function return the index of the elevator the call was allocated to
    def allocated_to(self) -> int:
        raise NotImplementedError
