class Employee:
    __id = 0
    __name = ''
    workers_list = []


    def check_name(self, name):
        self.__id += 1
        self.__name = name
        datatuple = (self.__id, self.__name)
        self.workers_list.append(datatuple)

    def printout(self):
        for x in range(0, len(self.workers_list)):
            print(f'Id: {self.workers_list[x][0]} Name: {self.workers_list[x][1]} ')



def main():
    workers = Employee()
    while True:
        user_input = str(input('Please enter employee name (0 to quit): '))
        if user_input == '0':
            workers.printout()
            break
        workers.check_name(user_input)


if __name__ == "__main__":
    main()