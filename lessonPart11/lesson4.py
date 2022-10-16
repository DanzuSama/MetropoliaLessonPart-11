class PayrollSystem:
    #accepts the list and printing it in the desired format
    def __init__(self, list):
        self.list = list

    def calculate_payroll(self):
        for x in range(0, len(self.list)):
            print('Employee Payroll\n================')
            print(f'Payroll for: {self.list[x][0]} - {self.list[x][1]}\n- Check amount: {self.list[x][2]}\n')

class Employee:
    __id = 0
    __name = ''
    workers_list = []

    def check_name(self, name, salary):
        self.__id += 1
        self.__name = name
        data = (self.__id, self.__name, salary)
        self.workers_list.append(data)


class SalaryEmployee(Employee):
    __monthly_salary = 0

    # method return salary employee
    def calculate_salary(self):
        user_input_salary = int(input('Please enter salary:'))
        self.__monthly_salary = user_input_salary
        return self.__monthly_salary


def main():
    workers = SalaryEmployee()
    while True:
        user_input = str(input('Please enter employee name (0 to quit):'))
        if user_input == '0':
            printing = PayrollSystem(Employee.workers_list)
            printing.calculate_payroll()
            break
        salary = workers.calculate_salary()
        workers.check_name(user_input, salary)


if __name__ == "__main__":
    main()
