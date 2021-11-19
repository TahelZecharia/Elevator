
from InterfaceCall import InterfaceCall


class Call(InterfaceCall):

    def __init__(self, name: str, time: float, src: int, dest: int, status: int, allocate_to: int):
        self.__name = name
        self.__time = time
        self.__src = src
        self.__dest = dest
        self.__status = status
        self.__allocated_to = allocate_to
        self.__got_to_src: bool = False
        self.__got_to_dest: bool = False
        self.__got_src_time: float = 0.
        self.__got_dest_time: float = 0.
        self.__type = "Up" if (self.__dest - self.__src) > 0 else "Down"

    def get_time(self) -> float:
        return self.__time

    def get_type(self) -> str:
        return self.__type

    def get_src(self) -> int:
        return self.__src

    def get_got_to_src(self) -> bool:
        return self.__got_to_src

    def set_got_to_src(self):
        self.__got_to_src = True

    def get_got_src_time(self) -> float:
        return self.__got_src_time

    def set_got_src_time(self, got_src_time):
        self.__got_src_time = got_src_time

    def get_dest(self) -> int:
        return self.__dest

    def get_got_to_dest(self) -> bool:
        return self.__got_to_dest

    def set_got_to_dest(self):
        self.__got_to_dest = True

    def get_got_dest_time(self) -> float:
        return self.__got_dest_time

    def set_got_dest_time(self, got_dest_time):
        self.__got_dest_time = got_dest_time

    def set_allocated_to(self, elev: int):
        self.__allocated_to = elev

    def allocated_to(self) -> int:
        return self.__allocated_to

    def __repr__(self) -> str:
        return f"time:{self.__time}, src:{self.__src}, " \
               f"dest:{self.__dest}, allocated To:{self.__allocated_to}, " \
               f"got to src:{self.__got_to_src}, got_to_dest: {self.__got_to_dest}, " \
               f"got_src_time: {self.__got_src_time}, got_dest_time: {self.__got_dest_time}"

    def __str__(self) -> str:
        return f"time:{self.__time}, src:{self.__src}, " \
               f"dest:{self.__dest}, allocated To:{self.__allocated_to}, " \
               f"got to src:{self.__got_to_src}, got_to_dest: {self.__got_to_dest}, " \
               f"got_src_time: {self.__got_src_time}, got_dest_time: {self.__got_dest_time}"

