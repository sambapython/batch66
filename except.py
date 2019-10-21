print("started")
a=input("Enter a number:")
b=input("Enter b number:")
print(f"before conversion a={a},b={b}")
try:
    a=float(a)
    b=float(b)
    print(f"after conversion a={a},b={b}")
    res=a/b
    print(f"res={res}")
except ZeroDivisionError as err:
    print("\tIssue in your input")
    print("\tb!=0")
except ValueError as err:
    print("\tIssue in your input")
    print("\texpecting only numbers")
except Exception as err:
    print("\tsome error")
    print("\t",err)
except:
    print("except")
    print("some ISSUE")
print("ended")
print("main block continues")