# Michelle Patlan
# 8/20/2022
#Problem 4: Write a Python function that takes a list of numbers and returns a new list with
#unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append
#function

def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1, 3, 3, 3, 6, 2, 3, 5]))