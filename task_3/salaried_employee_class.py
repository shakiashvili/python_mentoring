from dataclasses import dataclass
from employee_class import Employee


@dataclass
class SalariedEmployee(Employee):
    _salary: int = 0

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, salary) -> None:
        self._salary = salary

    def calculate_payment(self) -> float:
        return self._salary / 4