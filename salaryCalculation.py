#decorator for valid ctc
def ctcShouldGreatarThanZero(ctcFunction):
    def wrapperFunction():
        if(my_salary.get("ctc")>0):
            return ctcFunction()
        else:
            raise Exception("Please Enter Valid Ctc")
    return wrapperFunction

#decorator for valid salartuy structure type
def validType(salaryFunction):
    def validTypeWrapperFunction(type):
        if type == 1 or type == 2:
            return salaryFunction(type)
        else:
            raise Exception("Invalid Salary Type")
    return validTypeWrapperFunction

#class for salarystructure one
class SalaryDetailsOne:
    def __init__(self):
        self. monthlySalary = my_salary.get("ctc")/12
        self.basicSalary = self.monthlySalary*0.5
        self.houseRent =self.basicSalary*0.5
        self.employeePf = 1800
    def __str__(self):
        return "1"


#class for salary structure two
class SalaryDetailsTwo:
    def __init__(self):
        self. monthlySalary = my_salary.get("ctc")/12
        self.basicSalary = self.monthlySalary * 0.5
        self.houseRent = self.basicSalary
        if(self.basicSalary<= 15000):
            self.basicSalary = 15000
            self.houseRent = 0
        self.employeePf = 1800
    def __str__(self):
        return "2"



#function for calculating the salary based on type
@validType
def SalaryCalculation(type):
    SalaryStructureOne() if type == 1 else SalaryStructureTwo()

#assigning the existing values into the dictionary
def returnTheBasicDetails(salary):
    my_salary['Basic Salary']=salary.basicSalary
    my_salary['Monthly Salary']=salary.monthlySalary
    my_salary['HRA']=salary.houseRent
    my_salary['Employee PF']=salary.employeePf


#salary structure one calcualtion
@ctcShouldGreatarThanZero
def SalaryStructureOne():
    salaryDetails = SalaryDetailsOne()
    returnTheBasicDetails(salaryDetails)

#salary structure two calcualtion
@ctcShouldGreatarThanZero
def SalaryStructureTwo():
    salaryDetails = SalaryDetailsTwo()
    returnTheBasicDetails(salaryDetails)


#display the salary structure
def displaySalaryDetails():

    print("******************SALARY SLIP***********************")
    print("Employee Id",my_salary.get("id"))
    print("UAN No:***********")
    print("Employee Name: ", my_salary.get("name"))
    for detail in my_salary:
        if detail != "id" and detail != "ctc" and detail != "name":
            print(detail,":", my_salary.get(detail))
    print("******************************************************")
    print("Total CTC:", my_salary.get("ctc"))



global my_salary
my_salary = {}
my_salary['id']= input("Enter the employee id")
my_salary["name"]=input("Enter the employee name")
typeOfSalaryStructure = int(input("Enter the type of salary structure (Expected input should be either 1 or 2)"))
my_salary['ctc']= int(input("Please enter the total annual salary"))
SalaryCalculation(typeOfSalaryStructure)
extra_addon= True
while(extra_addon):
    extraAllowanceQuestion=int(input("Do you have any extra allowance, Please enter 1. Yes 2. No"))
    if(extraAllowanceQuestion == 1):
        allowanceName = input("Type of allowance")
        percentage = int(input("Percentage of allowance with annual ctc"))
        calculation = my_salary.get("ctc")*(percentage/100)
        my_salary[allowanceName]=calculation
    else:
        extra_addon=False


displaySalaryDetails()
