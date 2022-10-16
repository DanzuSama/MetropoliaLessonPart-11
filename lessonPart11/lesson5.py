# my_join : which joins list given as first argument to a string
# separated with character given as second argument.
# Function returns a string.

def my_join(my_list, insert):
    my_text = ''
    for x in range(len(my_list)):
        my_text += my_list[x]
        if x + 1 != len(my_list):
            my_text += insert
    return my_text


# my_split : my_split : which splits sentence given as first argument
# using second argument as a separator character to separate list items.
# Function returns a list of items.
def my_split(text, sim):
    list = []
    temp = ''
    for x in range(len(text)):
        if text[x] != sim:
            temp += text[x]
        if text[x] == sim:
            list.append(temp)
            temp = ''
        if x + 1 == len(text) and text[x] != sim:
            list.append(temp)
    return list


sentence = str(input('Please enter sentence: '))
print(my_join(my_split(sentence, ' '), ','))
print(my_join(my_split(sentence, ' '), '\n'))