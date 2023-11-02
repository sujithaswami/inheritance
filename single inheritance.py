class address:
    __address. str = " "
    def addAddress(self, address):
        self.__address = address
    def getAddress(self):
        return self.__address
class Employee:
    __firstName:str = " "
    __lastName: str = " "
    __surName: str = " "
    def setName(selfself, fName:str, lName:str, sName:str = " "):
        self. __firstName:str = fName
        self.__surName: str = sName
        self.__lastName: str = lName
    def --nameFormat(self):
    return f'{  self. __firstName} {self.__lastName} {self.__surName}'
    def getName(self):
        return self.__nameFormat()
emp = Employee
emp.setName(fName="suji", lName ="swami", sName="s")
emp.address("hyd")
print(emp.getFullName())

print(emp.getAddress())

