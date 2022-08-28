
class SalaryDetailsOne:
    def __init__(self,ctc):
        self. monthlySalary = ctc/12
        self.basicSalary = self.monthlySalary*0.5
        self.houseRent =self.basicSalary*0.5


class SalaryDetailsTwo:
    def __init__(self,ctc):
        self. monthlySalary = ctc/12
        self.basicSalary = self.monthlySalary * 0.5
        self.houseRent = self.basicSalary * 0.4
        if(self.basicSalary<= 15000):
            self.basicSalary = 15000
            self.houseRent = 0


def ctcShouldGreatarThanZero(ctcFunction):
    def wrapperFunction(ctc):
        if(ctc>0):
            return ctcFunction(ctc)
        else:
            raise Exception("Please Enter Valid Ctc")
    return wrapperFunction



def SalaryCalculation(type,ctc):
    if type == 1:
        SalaryStructureOne(ctc)
    else:
        SalaryStructureTwo(ctc)

def returnTheBasicDetails(salary):
    global my_salary
    my_salary = {'basic':salary.basicSalary,'monthly':salary.monthlySalary,'hra':salary.houseRent}


@ctcShouldGreatarThanZero
def SalaryStructureOne(ctc):
    salaryDetails = SalaryDetailsOne(ctc)
    returnTheBasicDetails(salaryDetails)



@ctcShouldGreatarThanZero
def SalaryStructureTwo(ctc):
    salaryDetails = SalaryDetailsOne(ctc)
    returnTheBasicDetails(salaryDetails)



def additionalInformation():
    print("addition Information")






typeOfSalaryStructure = int(input("Enter the type of salary structure"))
ctc= int(input("Please enter the total annual salary"))
SalaryCalculation(typeOfSalaryStructure,ctc)
extra_addon= True
while(extra_addon):
    extraAllowanceQuestion=int(input("Do you have any extra allowance, Please enter 1. Yes 2. No"))
    if(extraAllowanceQuestion == 1):
        allowanceName = input("Type of allowance")
        percentage = int(input("Percentage of allowance with annual ctc"))
        calculation = ctc*(percentage/100)
        my_salary[allowanceName]=calculation
    else:
        extra_addon=False


print(my_salary)


