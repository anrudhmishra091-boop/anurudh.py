# fuctons for operators
# user input
# print result
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def devide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def average(num1, num2):
    return num1 % num2


def square(num1, num2):
    return num1 ** num2


print("you can do those operattions on this : \n" 
      "1 addition "

          "2. substract" \
         
      "3.devide" \
      
      "4.average" \
      
      "5.square" \
      
      "6.multiply")


select = int(input("perform atleast one operation and select anyone :\n" \
"1,2,3,4,5,6 :"))



num1 = float(input("enter number 1"))

num2 = float(input("enter number"))




if select == 1:  

                    print(num1  +  num2)

if select == 2:
      print(num1 - num2)


if select == 3:

      print(num1 / num2)

if select == 4:
      print((num1 + num2)/"2")


if select == 5:
      print(num1 ** num2)

if select == 6:
      print(num1 * num2)


      if select > 6:
            print("invalid number entered")


if select > 6: 
      print("invalid")




if select < 1:
      print("invalid")

