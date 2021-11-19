
class InterfaceCall:

    def get_time(self) -> float:
        raise NotImplementedError

    def get_type(self) -> str:
        raise NotImplementedError

    def get_src(self) -> int:
        raise NotImplementedError

    def get_got_to_src(self) -> bool:
        raise NotImplementedError

    def set_got_to_src(self):
        raise NotImplementedError

    def get_got_src_time(self) -> float:
        raise NotImplementedError

    def set_got_src_time(self, got_src_time):
        raise NotImplementedError

    def get_dest(self) -> int:
        raise NotImplementedError

    def get_got_to_dest(self) -> bool:
        raise NotImplementedError

    def set_got_to_dest(self):
        raise NotImplementedError

    def get_got_dest_time(self) -> float:
        raise NotImplementedError

    def set_got_dest_time(self, got_dest_time):
        raise NotImplementedError

    def set_allocated_to(self, elev: int):
        raise NotImplementedError

    def allocated_to(self) -> int:
        raise NotImplementedError



