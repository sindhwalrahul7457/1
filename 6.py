#   Q6. Create a list containing 25 int type data. Using for loop and if-else condition print if the element is
# divisible by 3 or not.
list_1 = [1,23,45,65,43,54,45,4543,766,454,33,44,55,66,32,456,76,655,322,454,234,4564,345,34,9]
for i in range(len(list_1)):
    if list_1[i] % 3 == 0:
        print(f"{list_1[i]} is divisible by 3")
    else:
        print(f"{list_1[i]} is not divisible by 3")
