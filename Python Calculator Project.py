#Addition_Function--------
def addition(a,b):
    c=a+b
    return c    

#Subtraction_Function--------
def subtraction(a,b):
    c=a-b
    return c

#Multiplication_Function--------
def multiplication(a,b):
    c=a*b
    return c

#Division_Function--------
def division(a,b):
    c=a/b
    return c

#Main_Function--------------
def again():
    while True:
        #input_section
        try:
            a = int(input("\tEnter First Number "))
            b = int(input("\tEnter Second Number "))
        except:
            print("\tWrong Input Try Again")
            again()
        else:
            ch = int(input('''
            Welcome To The Calculator
            1>Addition        2>Subtraction
            3>Multiplication  4>Division
            5>Exit
            May I Know Your Choice ? '''))
            #Condition_Section
            if ch==1:
                c=addition(a,b)
                print(f"\n\tAddition of {a} + {b} = {c}")
                c_x = int(input("\tPress Any Key\n\t1>Continue\t2>Exit"))
                if c_x==1:
                    again()
                elif c_x==2:
                    print("\tThank You for Using")
                    break
                else:
                    print("\tWrong Input Exiting......")
                    break
            elif ch==2:
                c=subtraction(a,b)
                print(f"\n\tSubtraction of {a} + {b} = {c}")
                c_x = int(input("\tPress Any Key\n\t1>Continue\t2>Exit"))
                if c_x==1:
                    again()
                elif c_x==2:
                    print("\tThank You for Using")
                    break
                else:
                    print("\tWrong Input Exiting......")
                    break
            elif ch==3:
                c=multiplication(a,b)
                print(f"\n\tMultiplication of {a} + {b} = {c}")
                c_x = int(input("\tPress Any Key\n\t1>Continue\t2>Exit"))
                if c_x==1:
                    again()
                elif c_x==2:
                    print("\tThank You for Using")
                    break
                else:
                    print("\tWrong Input Exiting......")
                    break
            elif ch==4:
                c=division(a,b)
                print(f"\n\tDivision of {a} + {b} = {c}")
                c_x = int(input("\tPress Any Key\n\t1>Continue\t2>Exit"))
                if c_x==1:
                    again()
                elif c_x==2:
                    print("\tThank You for Using")
                    break
                else:
                    print("\tWrong Input Exiting......")
                    break
            elif ch==5:
                print("\tThank You for Using")
                break
            else:
                print("\tInviled Input Try Again")
        finally:
            print("\tThank You")
            break
again()
