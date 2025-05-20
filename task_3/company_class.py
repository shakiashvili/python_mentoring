from dataclasses import dataclass
from employee_class import Employee
from hourly_employee_class import HourlyEmployee
from salaried_employee_class import SalariedEmployee
from domain_class import Domain


@dataclass
class Company:
    name: str
    domain: Domain
    employees: list

    def hire(self, employee: Employee) -> None:
        if employee in self.employees:
            print(f"{employee.name} is already employed by {self.name}.")
        elif employee.company is not None:
            print(f"{employee.name} is already employed by another company.")
        else:
            self.employees.append(employee)
            employee.company = self

    def fire(self, employee: Employee) -> None:
        if employee in self.employees:
            self.employees.remove(employee)
            employee.company = None
        else:
            print(f"Employee is not employed by the {self.name}.")

    def raise_pay(self, employee: Employee, amount: int) -> None:
        if employee in self.employees:
            if isinstance(employee, SalariedEmployee):
                employee.salary += amount
            elif isinstance(employee, HourlyEmployee):
                employee.hourly_rate += amount
        else:
            print(f"{employee.name} is not employed by {self.name}.")

    def __repr__(self) -> str:
        return f"""Company({self.name}, {self.domain.name},
        Employees: {len(self.employees)})"""