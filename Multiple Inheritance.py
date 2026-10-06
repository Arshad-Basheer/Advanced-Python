class Hospital:
    def __init__(self):
        self.hname=input("Enter the hospital name:")
        self.loc=input("Enter the location:")
    def showDetails(self):
        print(f"Hospital name:{self.hname}")
        print(f"Hospital location:{self.loc}")

class Department:
    def __init__(self):
        self.dname=input("Enter department name:")
        self.drname=input("Enter doctor name:")
    def showDeptDetails(self):
        print(f"Department name:{self.dname}")
        print(f"Doctor's name:{self.drname}")

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.pid=(input("Enter patient id:"))
        self.pname=input("Enter patient name:")
        self.gender=input("Enter patient's gender:")
        self.place=input("Enter place:")
        self.adate=input("Enter admission date:")
        self.ddate=""
    def setDischargeDate(self):
        self.ddate=input("Enter discharge date:")
    def fullSummary(self):
        Hospital.showDetails(self)
        Department.showDeptDetails(self)
        print(f"Patient id:{self.pid}")
        print(f"Patient name:{self.pname}")
        print(f"Gender={self.gender}")
        print(f"Place:{self.place}")
        print(f"Admission date:{self.adate}")
        if self.ddate=="":
            print("Not yet discharged")
        else:
            print(f"Discharge date:{self.ddate}")
    def dischargeDetails(self):
        Hospital.showDetails(self)
        Department.showDeptDetails(self)
        print(f"Patient id:{self.pid}")
        print(f"Admission date:{self.adate}")
        if self.ddate=="":
            print("Not yet discharged")
        else:
            print(f"Discharge date:{self.ddate}")

p=Patient()
p.fullSummary()
p.setDischargeDate()
p.fullSummary()