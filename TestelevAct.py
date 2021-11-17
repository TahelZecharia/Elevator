import unittest
import copy

from Ex1.buildTry import Building
from Ex1.callListTry import CallsList
from callTry import Call
from elevTry import Elevator
from elevActTry import ElevatorAction


class TestElev(unittest.TestCase):

    def test_simulation(self):
        # 1) load call list
        # print('Enter your Calls:')
        # call = input()
        cl = CallsList()
        # cl.loadCSV(call)
        cl.loadCSV("Calls_a.csv")

        # 2) load building
        # print('Enter your build:')
        # build_input = input()
        build: Building = Building()
        # build.loadJson(build_input)
        build.loadJson("B2.json")

        print(len(cl.getCallList()))
        e = build.getElevator(0)
        # print(e)
        # print(cl.getCall(3))
        e.getCallsListOfElevator().append(cl.getCall(0))

        elev: ElevatorAction = ElevatorAction(e)
        self.assertEqual(elev.all_calls_list, e.getCallsListOfElevator())


if __name__ == '__main__':
    unittest.main()
