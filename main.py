list1 = "press 1 for addition"
list2 = "press 2 for subtraction"
list3 = "press 3 for multiplication"
list4 = "press 4 for division"
print(f" {list1} \n {list2} \n {list3} \n {list4}")

try:
    number = int(input("enter your choice :"))
    if number == 1:
      print("enter the first number :")
      a = int(input())
      print("enter the second number :")
      b = int(input())
      print(f"the addition of {a} and {b} = {a+b}")
    elif number == 2:
      print("enter the first number :")
      a = int(input())
      print("enter the second number :")
      b = int(input())
      print(f" {a} - {b} = {a-b}")
    elif number == 3:
      print("enter the first number")
      a = int(input())
      print("enter the second number")
      b = int(input())
      print(f" {a} x {b} = {a*b}")
    elif number == 4:
      print("enter the first number")
      a = int(input())
      print("enter the second number")
      b = int(input())
      print(f" {a} x {b} = {a / b}")
    else:
      print("enter a valid number")
except ValueError:
  print("enter a valid number")