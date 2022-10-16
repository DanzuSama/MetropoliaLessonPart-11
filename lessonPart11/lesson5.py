#my_join : который соединяет список, заданный в качестве первого аргумента, со строкой,
# разделенной символом, заданным в качестве второго аргумента. Функция возвращает строку.
def my_join():
    print()

#my_split : который разбивает предложение, указанное в качестве первого аргумента,
# используя второй аргумент в качестве символа-разделителя для разделения элементов списка.
# Функция возвращает список элементов.
def my_split(text, sim):
    list = []
    print(type(text))
    print(list)




x = 'This is a sentence'
print(my_split(x, ' '))




'''
sentence = str(input('Please enter sentence: '))
print(my_join(my_split(sentence,' '),','))
print(my_join(my_split(sentence,' '),'\n'))
'''