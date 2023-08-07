print("in the name of  Allah")
print("we are here to help you to solve Quadratic equations if you want our help enter Y if you dont enter N")

def Quadratic_equations():
    pass
while True:
    user_selection = input("enter your selection :")
    if user_selection == "Y" :
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
        delta = a**2 - 4*b*c
        if a == 0 :
            x = - c  /  b 
            print("x has one answer : " , x)
        if delta == 0 :
            x = b / (2*a)
            print("x has one answer : " , x)
        if delta < 0 :
            print("there is no answer for your Quadratic equations")
        if delta >0 :
            x1 = (-b + delta**1/2) / (2*a)
            x2 = (-b - delta**1/2) / (2*a)
            print("there are two answers : ")
            print(x1)
            print(x2)
    if user_selection == "N" :
        print("see you again")
        break
    else:
        print("wrong selection please try again")
