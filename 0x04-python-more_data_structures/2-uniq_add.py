#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = sum(set(my_list))
    return (uniq_list)

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

    #num = 0

    #for i in uniq_list:
        #num += i

    #return (num)
