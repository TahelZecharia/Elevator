import copy

from Ex1.Call import Call
from Ex1.ElevatorAct import ElevatorAction
from Ex1.Elevator import Elevator


# This is the main plan given that an elevator runs it and pretends it is in action
def sim(ele: Elevator) -> ElevatorAction:
    cur_time: float = 0
    elev: ElevatorAction = ElevatorAction(ele)
    while elev.get_num_of_done_calls() != len(elev.get_all_calls_list()):
        # giving the current time to the elevator
        elev.set_cur_time(cur_time)
        # calling the simulation method.
        elev.simulation()
        # updating the current time based on what happened in this round of the simulation
        cur_time += elev.update_time()
        # each time we advance the simulator by a second
        cur_time += 1
    return elev


# This function receives an elevator and call
# returns the time the call will add to the
# elevator if the reading was in the elevator
def cost(ele: Elevator, ele_act: ElevatorAction, cal: Call) -> float:
    elev: Elevator = copy.deepcopy(ele)
    elev.add_calls(cal)
    elev_act: ElevatorAction = sim(elev)
    return elev_act.get_time_for_calls() - ele_act.get_time_for_calls()
