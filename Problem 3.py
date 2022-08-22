# Michelle Patlan
# 8/20/2022
# Problem 3: Write a Python function to multiply all the numbers in a list. Use list [5, 2, 7,
# -1].

#setting up function
#start with 1 and it will return the product so it will be multiplied next
def multiply_list(list_num):
    result = 1
    for n in list_num:
        result = result * n
    return result


list_num = [5, 2, 7, -1]

print(multiply_list(list_num))

