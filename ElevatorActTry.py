import copy

from Call import Call
from Elevator import Elevator


class ElevatorAction:

    def __init__(self, elev: Elevator):
        self.__id: int = elev.get_ID()
        self.__speed: float = elev.get_speed()
        self.__minFloor: int = elev.get_min_floor()
        self.__maxFloor: int = elev.get_max_floor()
        self.__closeTime: float = elev.get_close_time()
        self.__openTime: float = elev.get_open_time()
        self.__startTime: float = elev.get_start_time()
        self.__stopTime: float = elev.get_stop_time()
        self.__cur_floor: int = 0
        self.__flag = "LEVEL"
        self.__cur_time: float = 0.
        self.__all_calls_list: list = elev.get_calls_list()
        self.__num_of_calls: int = 0
        self.__calls_to_do: list = copy.deepcopy(elev.get_calls_list())
        self.__curr_calls_list: list = []
        self.__done_calls_list: list = []
        self.__num_of_done_calls: int = 0
        self.__time_for_calls: float = 0
        self.__action_time = 0
        self.__test = 0
        self.__update_action_list: set = set()

    # This is run once before the simulation begins to set the time
    def get_flag(self):
        return self.__flag

    def get_curr_calls(self):
        return self.__curr_calls_list

    def get_ID(self):
        return self.__id

    def get_cur_floor(self):
        return self.__cur_floor

    def set_cur_time(self, cur_time):
        self.__cur_time = cur_time

    def set_sim_time_for_calls(self, time):
        self.sim_time_for_calls = time

    def get_sim_time_for_calls(self) -> float:
        return self.sim_time_for_calls

    def get_num_all_calls(self) -> int:
        return len(self.__all_calls_list)

    def get_time_for_calls(self) -> float:
        return self.__time_for_calls

    def get_cur_time(self) -> float:
        return self.__cur_time

    def add_call(self, call: Call):
        self.__all_calls_list.append(call)
        self.__calls_to_do.append(call)
        self.__num_of_calls += 1

    def get_done_list(self):
        return self.__done_calls_list

    def get_num_of_done_calls(self):
        return self.__num_of_done_calls

    def get_all_calls_list(self):
        return self.__all_calls_list

    # This is run once before the simulation begins to create the "all passenger list"
    def set_all_calls_list(self, all_calls_list):
        self.__all_calls_list = all_calls_list

    # This is used to make an action, like someone getting on the elevator, take more time
    def update_time(self) -> float:
        return self.__action_time

    def update_action_time(self, floor):
        if floor not in self.__update_action_list:
            self.__action_time += self.__stopTime + self.__openTime + self.__closeTime + self.__startTime
            self.__update_action_list.add(floor)

    def move(self, direction):
        if direction == "Up":
            self.__cur_floor += self.__speed
            for call in self.__curr_calls_list:
                if (not call.get_got_to_src()) and (self.__cur_floor > call.get_src()) \
                        and ((self.__cur_floor - self.__speed) <= call.get_src()):
                    self.update_action_time(call.get_src())
                    if self.__test: print("get src")
                    self.new_passenger(call)
            for call in self.__curr_calls_list:
                if call.get_got_to_src() and (self.__cur_floor > call.get_dest()) \
                        and ((self.__cur_floor - self.__speed) <= call.get_dest()):
                    self.update_action_time(call.get_dest())
                    if self.__test: print("get dest")
                    self.passenger_exit(call)
            if self.__test: print("^ moved up ^")
        else:
            self.__cur_floor -= self.__speed
            for call in self.__curr_calls_list:
                if (not call.get_got_to_src()) and (self.__cur_floor < call.get_src()) \
                        and ((self.__cur_floor + self.__speed) >= call.get_src()):
                    self.update_action_time(call.get_src())
                    if self.__test: print("get src")
                    self.new_passenger(call)
            for call in self.__curr_calls_list:
                if call.get_got_to_src() and (self.__cur_floor < call.get_dest()) \
                        and ((self.__cur_floor - self.__speed) >= call.get_dest()):
                    self.update_action_time(call.get_dest())
                    if self.__test: print("get src")
                    self.passenger_exit(call)
            if self.__test: print("v moved down v")

    # A method that changes the direction of the elevator
    def change_direction(self):
        if self.__flag == "Up":
            self.__flag = "Down"
        else:
            self.__flag = "Up"

    def new_passenger(self, call: Call):
        call.set_got_to_src()
        call.set_got_src_time(self.__cur_time)
        if self.__test: print("new passenger")

    def passenger_exit(self, call: Call):
        call.set_got_to_dest()
        call.set_got_dest_time(self.__cur_time)
        self.__done_calls_list.append(call)
        self.__curr_calls_list.remove(call)
        self.__time_for_calls += (call.get_got_dest_time() - call.get_time())
        self.__num_of_done_calls += 1
        if self.__test: print("exit passenger")

    def simulation(self):
        # It then updates the button list, from the action list, adding all actions since it has last been checked
        self.__action_time = 0
        self.__update_action_list = set()

        if len(self.__calls_to_do) != 0:
            for call in self.__calls_to_do:
                if call.get_time() <= self.__cur_time:
                    self.__curr_calls_list.append(call)
                    self.__calls_to_do.remove(call)
                else:
                    break

        if len(self.__curr_calls_list) == 0:
            return

        for call in self.__curr_calls_list:
            if (not call.get_got_to_src()) and (self.__cur_floor == call.get_src()):
                self.update_action_time(call.get_src())
                if self.__test: print("get src")
                self.new_passenger(call)

        for call in self.__curr_calls_list:
            if call.get_got_to_src() and (self.__cur_floor == call.get_dest()):
                self.update_action_time(call.get_src())
                self.passenger_exit(call)
                if self.__test: print("get dest")

        if len(self.__curr_calls_list) == 0:
            return

        if self.__flag == "LEVEL":
            c: Call = self.__curr_calls_list[0]
            if not c.get_got_to_src():
                if c.get_src() < self.__cur_floor:
                    self.__flag = "Down"
                else:
                    self.__flag = "Up"
            else: self.__flag = c.get_type()
            if self.__test: print(self.__flag)

        # the elevator moves to the most extreme person waiting in its direction of travel.
        if self.__flag == "Up":
            temp_goal = max(call.get_src() for call in self.__curr_calls_list)
            for call in self.__curr_calls_list:
                if call.get_type() == "Up":
                    if call.get_got_to_src():
                        if call.get_dest() > temp_goal:
                            temp_goal = call.get_dest()
            if temp_goal > self.__cur_floor:
                goal = temp_goal
            elif temp_goal < self.__cur_floor:
                self.change_direction()
                temp_goal_src = min(call.get_src() for call in self.__curr_calls_list)
                temp_goal_dest = min(call.get_dest() for call in self.__curr_calls_list)
                goal = min(temp_goal_dest, temp_goal_src)
            else:
                goal = self.__cur_floor
        else:
            temp_goal = min(call.get_src() for call in self.__curr_calls_list)
            for call in self.__curr_calls_list:
                if call.get_type() == "Down":
                    if call.get_got_to_src():
                        if call.get_dest() < temp_goal:
                            temp_goal = call.get_dest()
            if temp_goal < self.__cur_floor:
                goal = temp_goal
            elif temp_goal > self.__cur_floor:
                self.change_direction()
                temp_goal_src = max(call.get_src() for call in self.__curr_calls_list)
                temp_goal_dest = max(call.get_dest() for call in self.__curr_calls_list)
                goal = max(temp_goal_dest, temp_goal_src)
            else:
                goal = self.__cur_floor
        if self.__test: print("goal=", goal)
        if self.__test: print("cur_time", self.__cur_time)
        if self.__test: print("cur_floor", self.__cur_floor)
        if goal > self.__cur_floor and self.__flag == "Up":
            self.move("Up")
            if self.__test: print("1")
        elif goal > self.__cur_floor and self.__flag == "Down":
            self.__flag = "Up"
            self.move("Up")
            if self.__test: print("2")
        elif goal < self.__cur_floor and self.__flag == "Down":
            self.move("Down")
            if self.__test: print("3")
        elif goal < self.__cur_floor and self.__flag == "Up":
            self.__flag = "Down"
            self.move("Down")
            if self.__test:
                if self.__test: print("4")
        elif goal == self.__cur_floor:
            self.change_direction()
            if self.__test: print("5")

    def __str__(self) -> str:
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s," \
               "all_calls_list: %s, curr_call_list: %s, done_calls_list: %s," \
               "cur_floor: %s, flag: %s, cur_time: %s, action_time: %s " \
               % (self.__id, self.__speed, self.__minFloor, self.__maxFloor, self.__closeTime,
                  self.__openTime, self.__startTime, self.__stopTime, self.__all_calls_list,
                  self.__curr_calls_list, self.__done_calls_list, self.__cur_floor,
                  self.__flag, self.__cur_time, self.__action_time)