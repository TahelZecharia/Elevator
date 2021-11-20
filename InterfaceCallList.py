from Ex1.Call import Call

# This is an interface to a list that contains calls


class InterfaceCallList:

    # This is a function that receives a csv file and loads it into a CallList list
    def loadCSV(self, file_name):
        raise NotImplementedError

    # This is a function that loads a CallList list into a csv file
    def writeCSV(self):
        raise NotImplementedError

    # This is a function that gets an index and returns the call in that index
    def getCall(self, ind: int) -> Call:
        raise NotImplementedError

    # This is a function that receives a call and puts it on the list
    def add_call(self, call: Call):
        raise NotImplementedError

    # This is a function that receives a call and remove it from the list
    def remove_call(self, call: Call):
        raise NotImplementedError

    # This is a function that returns the call list
    def getCallList(self) -> list:
        raise NotImplementedError

    # This is a function that returns the len of the call list
    def get_len(self) -> int:
        raise NotImplementedError


