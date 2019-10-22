import logging
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s==>%(levelname)s==>%(name)s==>%(message)s")
#asctime,levelname,message,name
logging.info("****PROGRAM STARTED****")
a=input("Enter a number:")
b=input("Enter b number:")
logging.debug(f"before conversion a={a},b={b}")
try:
    a=float(a)
    logging.info("a converted")
    b=float(b)
    logging.info("b converted")
    logging.debug(f"after conversion a={a},b={b}")
    res=a/b
    print(f"res={res}")
    logging.debug(f"res={res}")
except ZeroDivisionError as err:
    logging.error(err)
    print("\tIssue in your input")
    print("\tb!=0")
except ValueError as err:
    logging.error(err)
    print("\tIssue in your input")
    print("\texpecting only numbers")
except Exception as err:
    logging.error(err)
    print("\tsome error")
    print("\t",err)
logging.info("ENDED")