#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for val in range(0, list_length):
        try:
            d = my_list_1[val] / my_list_2[val]
        except TypeError:
            print("Wrong type")
            d = 0
        except ZeroDivisionError:
            print("division by 0")
            d = 0
        except IndexError:
            print("out of range")
            d = 0
        finally:
            div_list.append(d)
    return (div_list)
