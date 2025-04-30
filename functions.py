from file_manager import read_data, write_data, append_data



def add():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sum = num1 + num2
    data = [num1,"+", num2,"=",sum]
    append_data(file_name="results.csv", data=data)
    print(f"{num1} + {num2} = {sum}")


def sub():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res = num1 - num2
    data = [num1,"-", num2,"=",res]
    append_data(file_name="results.csv", data=data)
    print(f"{num1} - {num2} = {res}")

def mult():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res = num1 * num2
    data = [num1,"*", num2,"=",res]
    append_data(file_name="results.csv", data=data)
    print(f"{num1} * {num2} = {res}")


def div():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res = num1 / num2
    data = [num1,"/", num2,"=",res]
    append_data(file_name="results.csv", data=data)
    print(f"{num1} / {num2} = {res}")