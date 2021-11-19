from Ex1.Call import Call


class InterfaceCallList:

    def loadCSV(self, file_name):
        raise NotImplementedError

    def writeCSV(self):
        raise NotImplementedError

    def getCall(self, ind: int) -> Call:
        raise NotImplementedError

    def add_call(self, call: Call):
        raise NotImplementedError

    def remove_call(self, call: Call):
        raise NotImplementedError

    def getCallList(self) -> list:
        raise NotImplementedError

    def get_len(self) -> int:
        raise NotImplementedError


