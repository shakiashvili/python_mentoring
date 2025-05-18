from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum


# 1. Employee Class
@dataclass
class Employee(ABC):
    name: str
    emp_id: str = None
    _company: str = field(default=None) 
    _last_assigned_id: int = 0

    def __post_init__(self):
        if self.emp_id is None:
            self.__class__._last_assigned_id += 1
            self.emp_id = f"E{self.__class__._last_assigned_id}"

    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    @abstractmethod
    def calculate_payment(self):
        pass

    def leave_company(self):
        if self._company:
            self._company.fire(self)
            self._company = None
        else:
            print(f"{self.name} is not currently employed by any company.")


@dataclass
class HourlyEmployee(Employee):
    _hourly_rate: int = 0

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate):
        self._hourly_rate = rate

    def calculate_payment(self):
        return self._hourly_rate * 40 


@dataclass
class SalariedEmployee(Employee):
    _salary: int = 0

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, salary):
        self._salary = salary

    def calculate_payment(self):
        return self._salary / 4


class Domain(Enum):
    TECHNOLOGY = "TECHNOLOGY"
    HEALTHCARE = "HEALTHCARE"
    RETAIL = "RETAIL"


@dataclass
class Company:
    name: str
    domain: Domain
    employees: list

    def hire(self, employee: Employee):
        if employee in self.employees:
            print(f"{employee.name} is already employed by {self.name}.")
        elif employee.company is not None:
            print(f"{employee.name} is already employed by another company.")
        else:
            self.employees.append(employee)
            employee.company = self

    def fire(self, employee: Employee):
        if employee in self.employees:
            self.employees.remove(employee)
            employee.company = None
        else:
            print(f"non employee of {self.name}.")

    def raise_pay(self, employee: Employee, amount: int):
        if employee in self.employees:
            if isinstance(employee, SalariedEmployee):
                employee.salary += amount
            elif isinstance(employee, HourlyEmployee):
                employee.hourly_rate += amount
        else:
            print(f"{employee.name} is not employed by {self.name}.")

    def __repr__(self):
        return f"""Company({self.name}, {self.domain.name},
        Employees: {len(self.employees)})"""


quant = Company(2, Domain.HEALTHCARE, ['Zaka', 'Zuka'])
epam = Company(1, Domain.TECHNOLOGY, ['Gio'])

emp1 = SalariedEmployee('Giorgi', 1, 'Epam')
emp3 = SalariedEmployee('Giorgi', 3)

emp2 = HourlyEmployee('Lekso', 2, 'Alexsoft')

quant.hire(emp3)
quant.hire(emp3)
quant.fire(emp3)

quant.fire('Lika')

emp3.salary = 50
print(emp3.calculate_payment())
quant.hire(emp3)

quant.raise_pay(emp3, 60)
print(emp3.calculate_payment())
emp3.leave_company()
print(quant) 
