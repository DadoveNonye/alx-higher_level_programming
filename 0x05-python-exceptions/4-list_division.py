#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length

    for i in range(list_length):
        try:
            result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            result[i] = 0
            print("division by 0")
        except (ValueError, TypeError):
            result[i] = 0
            print("wrong type")
        except IndexError:
            result[i] = 0
            print("out of range")
        finally:
            pass
    
    return result
