from Ex1.Call import Call

# It's an interface to a class that simulates an elevator in action


class InterfaceElevatorAct:
    # this is a function that gets a direction and move the elevator to it
    def move(self, direction):
        raise NotImplementedError

    # this is a function that changes the direction of the elevator
    def change_direction(self):
        raise NotImplementedError

    # this is a function that gets a call and updates that the call has reached the source
    def call_got_to_src(self, call: Call):
        raise NotImplementedError

    # this is a function that gets a call and updates that the call has reached the destination
    def call_got_to_dest(self, call: Call):
        raise NotImplementedError

    # This is the main program that moves the elevator
    # each time to where it needs to be according to the calls in the elevator
    def simulation(self):
        raise NotImplementedError
