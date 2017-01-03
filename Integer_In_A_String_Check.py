#Integer_In_a_Given_String_Check
x=input("Enter a String")
#Check Whether It is a Int
try:
    x=int(x)
    print("True")
#Check Whether It is a Float
except ValueError:
    try:
        x=float(x)
        print("True")
    except ValueError:
        print("False")
