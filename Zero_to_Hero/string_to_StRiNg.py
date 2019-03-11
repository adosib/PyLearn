def myfunc(my_string):
    new_string = ''
    for index, letter in enumerate(my_string):
        if index%2 == 0:
            new_string += my_string[index].upper()
        else:
            new_string += my_string[index].lower()
    return new_string

myfunc("garbage")
 