def get_num():
    num = int(input("Enter a number:"))
    return num

def add():
    num_1 = get_num()
    num_2 = get_num()
    sum = num_1 + num_2
    return sum

print("the sum of the numbers is " + str(add()))
