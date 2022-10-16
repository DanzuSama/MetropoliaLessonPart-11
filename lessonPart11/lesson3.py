
def bubble_sort(array):

    for i in range(len(array)):

        swapped = False

        for j in range(0, len(array) - i - 1):


            if array[j] > array[j + 1]:

                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

        if not swapped:
            return array
            break


a = []
number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element : " %i))
    a.append(value)
print("The Sorter List in Ascending Order : ", bubble_sort(a))