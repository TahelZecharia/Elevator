import copy
import math
from callTry import Call
from elevTry import Elevator


class ElevatorAction:

    def __init__(self, elev: Elevator):
        self.__id: int = elev.getID()
        self.__speed: float = elev.getSpeed()
        self.__minFloor: int = elev.getMinFloor()
        self.__maxFloor: int = elev.getMaxFloor()
        self.__closeTime: float = elev.getCloseTime()
        self.__openTime: float = elev.getOpenTime()
        self.__startTime: float = elev.getStartTime()
        self.__stopTime: float = elev.getStopTime()
        # Current floor the elevator is on
        self.cur_floor: int = 0
        # DOT = Direction Of Travel. Can be "Up" or "Down".
        self.flag = "LEVEL"
        # The people in the elevator
        # self.passengers_in_elevator_list = []
        # Sets the start time to zero
        self.cur_time: float = 0.
        # Counts the number of people who have reached their destination
        # self.happy_people = 0
        # List of all people who are in the simulation
        self.all_calls_list: list = copy.deepcopy(elev.getCallsListOfElevator())
        self.calls_to_do: list = copy.deepcopy(elev.getCallsListOfElevator())
        # The passengers who are waiting
        self.curr_calls_list: list = []
        self.done_calls_list: list = []
        # how much time an event takes... setting this to 4 would make that step take 4 seconds extra
        self.action_time = 0
        # last time it checked the passenger list to see if there are new buttons
        # self.last_check = 0
        # This is to know what the top floor is
        self.__num_of_done_calls: int = 0
        self.test = 0
        self.last_call: int = 0

    # This is run once before the simulation begins to set the time
    def set_cur_time(self, cur_time):
        self.cur_time = cur_time

    def get_done_list(self):
        return self.done_calls_list

    def get_num_of_done_calls(self):
        return self.__num_of_done_calls

    def get_all_calls_list(self):
        return self.all_calls_list

    # This is run once before the simulation begins to create the "all passenger list"
    def set_all_calls_list(self, all_calls_list):
        self.all_calls_list = all_calls_list

    # This is used to make an action, like someone getting on the elevator, take more time
    def update_time(self) -> float:
        return self.action_time

    def get_time_for_calls(self) -> float:
        time: float = 0.
        if len(self.done_calls_list) != 0:
            for call in self.done_calls_list:
                time += (call.get_got_dest_time() - call.get_time())
        return time

    # This moves the elevator .25 floors up in the indicated direction (moving up one floor takes 2 seconds)
    def move(self, direction):
        if direction == "Up":
            self.cur_floor += (1/self.__speed)
            if self.test: print("^ moved up ^")
        else:
            self.cur_floor -= (1/self.__speed)
            if self.test: print("v moved down v")

    # A method that changes the direction of the elevator
    def change_direction(self):
        if self.flag == "Up":
            self.flag = "Down"
        else:
            self.flag = "Up"

    # A method to add passengers to the elevator. It takes a list of passengers as an input
    # and the passengers who have waited the most enter first, either until there are no
    # more people waiting at that floor, or until the maximum capacity of the elevator is reached.
    def new_passenger(self, call: Call):
        call.set_got_to_src()
        call.set_got_src_time(self.cur_time)
        if self.test: print("new passenger")

    # A method used for passengers to get off the elevator at their desired floor.
    # It takes as input a list of passengers who want to exit and removes them from the elevator
    def passenger_exit(self, call: Call):
        call.set_got_to_dest()
        call.set_got_dest_time(self.cur_time)
        self.done_calls_list.append(call)
        self.curr_calls_list.remove(call)
        self.__num_of_done_calls += 1
        if self.test: print("exit passenger")

    # def update_last_check(self):
    #     self.last_check = self.cur_time

    def simulation(self):

        self.action_time = 0

        # It then updates the button list, from the action list, adding all actions since it has last been checked
        for call in self.calls_to_do:
            if call.get_time() <= self.cur_time:
                self.curr_calls_list.append(call)
                self.calls_to_do.remove(call)
                self.last_call += 1
            else:
                break

        if len(self.curr_calls_list) == 0:
            return

            # If a person is in the elevator and its on their floor, they should get off
        for call in self.curr_calls_list:
            if call.get_got_to_src() and math.floor(self.cur_floor) == call.get_dest():
                self.action_time = self.__stopTime + self.__openTime + self.__closeTime + self.__startTime
                self.passenger_exit(call)
                if self.test: print("get dest")

        # If a person is on the same level as the elevator and it is moving in their
        # direction of travel, they should get on
        for call in self.curr_calls_list:
            if (not call.get_got_to_src()) and math.floor(self.cur_floor) == call.get_src():
                self.action_time = self.__stopTime + self.__openTime + self.__closeTime + self.__startTime
                if self.test: print("get src")
                self.new_passenger(call)

        if len(self.curr_calls_list) == 0:
            return

        # The next is if there are no people in the elevator, but there are people waiting for the elevator.
        # In this case, the elevator moves to the most extreme person waiting in its direction of travel.
        if self.flag == "LEVEL":
            c: Call = self.curr_calls_list[0]
            if not c.get_got_to_src():
                if c.get_src() < self.cur_floor:
                    self.flag = "Down"
                else:
                    self.flag = "Up"
            else: self.flag = c.get_type()
            if self.test: print(self.flag)

        if self.flag == "Up":
            temp_goal_src = max(call.get_src() for call in self.curr_calls_list)
            temp_goal_dest = max(call.get_dest() for call in self.curr_calls_list)
            temp_goal = max(temp_goal_dest, temp_goal_src)
            if temp_goal > self.cur_floor:
                goal = temp_goal
            elif temp_goal < self.cur_floor:
                self.change_direction()
                temp_goal_src = min(call.get_src() for call in self.curr_calls_list)
                temp_goal_dest = min(call.get_dest() for call in self.curr_calls_list)
                goal = min(temp_goal_dest, temp_goal_src)
            else:
                goal = self.cur_floor
        else:
            temp_goal_src = min(call.get_src() for call in self.curr_calls_list)
            temp_goal_dest = min(call.get_dest() for call in self.curr_calls_list)
            # temp_goal_dest = min(call.get_dest() for call in [i for i in self.curr_calls_list if i is not None])
            temp_goal = min(temp_goal_dest, temp_goal_src)
            if temp_goal < self.cur_floor:
                goal = temp_goal
            elif temp_goal > self.cur_floor:
                self.change_direction()
                temp_goal_src = max(call.get_src() for call in self.curr_calls_list)
                temp_goal_dest = max(call.get_dest() for call in self.curr_calls_list)
                goal = max(temp_goal_dest, temp_goal_src)
            else:
                goal = self.cur_floor
        if self.test: print("goal=", goal)
        if self.test: print("cur_time", self.cur_time)
        if self.test: print("cur_floor", self.cur_floor)
        if goal > self.cur_floor and self.flag == "Up":
            self.move("Up")
            if self.test: print("1")
        elif goal > self.cur_floor and self.flag == "Down":
            self.flag = "Up"
            self.move("Up")
            if self.test: print("2")
        elif goal < self.cur_floor and self.flag == "Down":
            self.move("Down")
            if self.test: print("3")
        elif goal < self.cur_floor and self.flag == "Up":
            self.flag = "Down"
            self.move("Down")
            if self.test:
                if self.test: print("4")
        elif goal == self.cur_floor:
            self.change_direction()
            if self.test: print("5")

    def __str__(self) -> str:
        return "id: %s, speed: %s, min floor: %s," \
               "max floor: %s, close time: %s, open time: %s, start time: %s stop time: %s," \
               "all_calls_list: %s, curr_call_list: %s, done_calls_list: %s," \
               "cur_floor: %s, flag: %s, cur_time: %s, action_time: %s " \
               % (self.__id, self.__speed, self.__minFloor, self.__maxFloor, self.__closeTime,
                  self.__openTime, self.__startTime, self.__stopTime,  self.all_calls_list,
                  self.curr_calls_list, self.done_calls_list, self.cur_floor,
                  self.flag, self.cur_time, self.action_time)

        # Current floor the elevator is on






