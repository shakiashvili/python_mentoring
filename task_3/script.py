from Domain import Domain
from SalariedEmployee import SalariedEmployee
from HourlyEmployee import HourlyEmployee
from Company import Company


if __name__ == "__main__":
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
