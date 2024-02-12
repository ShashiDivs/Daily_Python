from dataclasses import dataclass,fields,asdict

@dataclass
class Employee:
    Name:str
    Designation:str
    Salary: int

employee1 = Employee("shashi","Data Scientist",80000)

# for i in fields(employee1):
#     print(i)

employee_dict = asdict(employee1)

for values in employee_dict.values():
    print(values)
