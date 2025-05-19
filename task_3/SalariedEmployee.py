from dataclasses import dataclass
from Employee import Employee


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
        return self._salary / 7