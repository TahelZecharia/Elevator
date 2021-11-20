from ElevatorActList import ElevatorActList
from Elevator import Elevator
from CallList import CallsList
from Building import Building
from Call import Call
from ElevatorAct import ElevatorAction
from Simulator import sim
from Simulator import cost

# this is the main program that gets a Jason file containing
# a building with elevators inside, and a csv file of calls,
# and returns a csv file of calls with the optimal placement
# for each call so that the average waiting time of all calls
# is as short as possible.

if __name__ == '__main__':

    # 1) load call list:
    calls_list = CallsList()
    final_calls_list = CallsList()
    calls_list.loadCSV("Calls_a.csv")

    # 2) load building
    build: Building = Building()
    build.loadJson("B2.json")

    # 3) creat an array of elevators of ElevatorAct
    elev_act_list: ElevatorActList = ElevatorActList()
    for i in range(0, build.getNumberOfElevators()):
        elevator: ElevatorAction = ElevatorAction(build.getElevator(i))
        elev_act_list.add_elev(elevator)

    # 4) go over all the calls and place them in the appropriate elevator:
    while calls_list.get_len() != 0:
        # first call
        print(calls_list.getCall(0))
        # variable placement with the first elevator:
        call: Call = calls_list.getCall(0)
        elev_index: int = 0
        min_time: float = cost(build.getElevator(0), elev_act_list.get_elev(0), call)
        # Go over all the elevators:
        for k in range(1, build.getNumberOfElevators()):
            temp: float = cost(build.getElevator(k), elev_act_list.get_elev(k), call)
            if temp < min_time:
                elev_index = k
                min_time = temp

        elevator: Elevator = (build.getElevator(elev_index))
        elevator.add_calls(call)
        elev_act_list.get_list()[elev_index]: ElevatorAction = sim(build.getElevator(elev_index))
        call.set_allocated_to(elev_index)
        final_calls_list.getCallList().append(call)
        calls_list.getCallList().remove(call)

    # 5) write csv:
    final_calls_list.writeCSV()