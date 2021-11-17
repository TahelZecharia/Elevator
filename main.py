import copy
from elevTry import Elevator
from callListTry import CallsList
from buildTry import Building
# from simTry import Simulator
from callTry import Call
from elevActTry import ElevatorAction


# def sim_floor(time: float, elev: Elevator) -> float:
#     cur_time: float = 0
#     # This is the main while loop for the simulation (if only running the simulation once,
#     # this is the only while loop needed)
#     ele: ElevatorAction = ElevatorAction(elev)
#     while cur_time <= time:
#         # Giving the current time to the elevator
#         ele.set_cur_time(cur_time)
#
#         # Calling the simulation method. It works with .simulation() or .simulation_2().
#         ele.simulation()
#
#         # Updating the current time based on what happened in this round of the simulation
#         cur_time += ele.update_time()
#
#         # Half a second passes at every round no matter what
#         cur_time += 0.5
#
#     return ele.cur_floor


def sim(ele: Elevator) -> ElevatorAction:
    cur_time: float = 0
    # This is the main while loop for the simulation (if only running the simulation once,
    # this is the only while loop needed)
    elevat: ElevatorAction = ElevatorAction(ele)
    # print(elevat)
    while elevat.get_num_of_done_calls() != len(elevat.get_all_calls_list()):
        # Giving the current time to the elevator
        elevat.set_cur_time(cur_time)

        # Calling the simulation method. It works with .simulation() or .simulation_2().
        elevat.simulation()

        # Updating the current time based on what happened in this round of the simulation
        cur_time += elevat.update_time()

        # Half a second passes at every round no matter what
        cur_time += 1

    return elevat


def cost(ele: Elevator, elevators_help: ElevatorAction, cal: Call) -> float:
    el2: Elevator = copy.deepcopy(ele)
    el2.getCallsListOfElevator().append(cal)
    # new_el1: ElevatorAction = sim(el1)
    new_el2: ElevatorAction = sim(el2)
    return new_el2.get_time_for_calls() - elevators_help.get_time_for_calls()


if __name__ == '__main__':

    # 1) load call list
    # print('Enter your Calls:')
    # call = input()
    cl = CallsList()
    # cl.loadCSV(call)
    cl.loadCSV("Calls_b.csv")

    # 2) load building
    # print('Enter your build:')
    # build_input = input()
    build: Building = Building()
    # build.loadJson(build_input)
    build.loadJson("B4.json")

    elevator_help: list = []
    for j in range(0, build.getNumberOfElevators()):
        elevator_help.append(sim(build.getElevator(j)))

    cl2 = CallsList()

    while len(cl.getCallList()) != 0:

        # first call
        print(cl.getCall(0))
        call: Call = cl.getCall(0)
        # for key,ele in build.getElevators().items():
        elev: int = 0
        min_time: float = cost(build.getElevator(0), elevator_help[0], call)
        for k in range(1, build.getNumberOfElevators()):
            # all elevators
            temp: float = cost(build.getElevator(k), elevator_help[k], call)
            if temp < min_time:
                elev = k
                min_time = temp
        elevator: Elevator = (build.getElevator(elev))
        elevator.getCallsListOfElevator().append(call)
        elevator_help[elev]: ElevatorAction = sim(build.getElevator(elev))
        new_call: Call = call
        new_call.set_allocated_to(elev)
        cl2.getCallList().append(call)
        cl.getCallList().remove(call)

    # 3) write csv
    cl2.writeCSV()

    # print(len(cl.getCallList()))
    # e = build.getElevator(0)
    # # print(e)
    # e.getCallsListOfElevator().append(cl.getCall(1))
    # e.getCallsListOfElevator().append(cl.getCall(2))
    # e.getCallsListOfElevator().append(cl.getCall(3))
    # e.getCallsListOfElevator().append(cl.getCall(4))
    # print(e.getCallsListOfElevator())
    # el = sim(e)

