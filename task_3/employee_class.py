from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass
class Employee(ABC):
    name: str
    emp_id: str = None
    _company: str = field(default=None) 
    _last_assigned_id: int = 0

    def __post_init__(self) -> None:
        if self.emp_id is None:
            self.__class__._last_assigned_id += 1
            self.emp_id = f"E{self.__class__._last_assigned_id}"

    @property
    def company(self) -> None:
        return self._company

    @company.setter
    def company(self, company: str) -> None: 
        self._company = company

    @abstractmethod
    def calculate_payment(self) -> None:
        pass

    def leave_company(self) -> None:
        if self._company:
            self._company.fire(self)
            self._company = None
        else:
            print(f"{self.name} is not currently employed by any company.")