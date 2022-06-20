#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            new_list.append(div)
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("zero division")
        except IndexError:
            div = 0
            print("index error")
        finally:
            new_list.append(div)
    return new_list
