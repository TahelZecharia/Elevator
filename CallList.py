import csv
from Call import Call
from InterfaceCallList import InterfaceCallList
# This class implements the CallList Interface


class CallsList(InterfaceCallList):

    def __init__(self):
        self.__callList = []

    def loadCSV(self, file_name):
        rows = []
        with open(file_name) as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                c = Call(name=str(row[0]), time=float(row[1]), src=int(row[2]),
                         dest=int(row[3]), status=int(row[4]), allocate_to=int(row[5]))
                self.__callList.append(c)
                rows.append(row)

    def writeCSV(self):
        newCallList = []
        for call in self.__callList:
            newCallList.append(call.__dict__.values())
        print(newCallList)
        filename = 'output.csv'

        with open(filename, 'w', newline="") as file:
            csvWriter = csv.writer(file)  # create a csvwriter object
            csvWriter.writerows(newCallList)  # write the data

    def getCall(self, ind: int) -> Call:
        return self.__callList[ind]

    def add_call(self, call: Call):
        self.__callList.append(call)

    def remove_call(self, call: Call):
        self.__callList.remove(call)

    def getCallList(self) -> list:
        return self.__callList

    def get_len(self) -> int:
        return len(self.__callList)

    def __str__(self) -> str:
        return f"list:{self.__callList.__repr__()}"
