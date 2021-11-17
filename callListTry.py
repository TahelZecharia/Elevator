import csv
from callTry import Call


class CallsList:

    def __init__(self):
        self.__callList = []

    def loadCSV(self, file_name):
        rows = []
        with open(file_name) as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                c = Call(name=str(row[0]), time=float(row[1]), src=int(row[2]),
                         dest=int(row[3]), status=int(row[4]), allocateTo=int(row[5]))
                self.__callList.append(c)
                rows.append(row)

    def getCall(self, ind: int) -> Call:
        return self.__callList[ind]

    def getCallList(self) -> list:
        return self.__callList

    def writeCSV(self):
        newCallList = []
        for call in self.__callList:
            newCallList.append(call.__dict__.values())
        print(newCallList)
        filename = 'output.csv'

        with open(filename, 'w', newline="") as file:
            csvWriter = csv.writer(file)  # create a csvwriter object
            csvWriter.writerows(newCallList)  # write the data

    def __str__(self) -> str:
        return f"list:{self.__callList.__repr__()}"


# if __name__ == '__main__':
#
#     cl = CallsList()
#     cl.loadCSV("Calls_a.csv")
#     print(cl.getCall(3))
#     print(cl)
#     cl.writeCSV()
