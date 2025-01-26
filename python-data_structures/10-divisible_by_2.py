#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    end = []
    for num in my_list:
        if num % 2 == 0:
            end.append(True)
        else:
            end.append(False)
    return end
