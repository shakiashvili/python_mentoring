from dataclasses import dataclass
from employee_class import Employee


@dataclass
class HourlyEmployee(Employee):
    _hourly_rate: int = 0

    @property
    def hourly_rate(self) -> int:
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate: int) -> None:
        self._hourly_rate = rate

    def calculate_payment(self) -> int:
        return self._hourly_rate * 40 