import copy
from Ex1 import buildTry
from callTry import Call
from elevTry import Elevator
from elevActTry import ElevatorAction


def sim_floor(time: float, elev: Elevator) -> float:
    cur_time: float = 0
    # This is the main while loop for the simulation (if only running the simulation once,
    # this is the only while loop needed)
    elevator: ElevatorAction = ElevatorAction(elev)
    while len(cur_time <= time):
        # Giving the current time to the elevator
        elevator.set_cur_time(cur_time)

        # Calling the simulation method. It works with .simulation() or .simulation_2().
        elevator.simulation()

        # Updating the current time based on what happened in this round of the simulation
        cur_time += elevator.update_time()

        # Half a second passes at every round no matter what
        cur_time += 0.5

    return elevator.cur_floor


def sim(elev: Elevator) -> ElevatorAction:
    cur_time: float = 0
    # This is the main while loop for the simulation (if only running the simulation once,
    # this is the only while loop needed)
    elevator: ElevatorAction = ElevatorAction(elev)
    while len(elev.getCallsListOfElevator()) < len(elevator.get_done_list()):
        # Giving the current time to the elevator
        elevator.set_cur_time(cur_time)

        # Calling the simulation method. It works with .simulation() or .simulation_2().
        elevator.simulation()

        # Updating the current time based on what happened in this round of the simulation
        cur_time += elevator.update_time()

        # Half a second passes at every round no matter what
        cur_time += 0.5

    return elevator


def cost(elev: Elevator, call: Call) -> float:
    el1: Elevator = copy.deepcopy(elev)
    el2: Elevator = copy.deepcopy(elev)
    el2.getCallsListOfElevator().append(call)
    new_el1: ElevatorAction = sim(el1)
    new_el2: ElevatorAction = sim(el2)
    return new_el2.get_time_for_calls() - new_el1.get_time_for_calls()










