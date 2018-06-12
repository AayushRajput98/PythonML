try:
    x = 10
    y = 0
    z = x / y
    print(z)
except (ArithmeticError,EOFError,ImportError,IndentationError,ModuleNotFoundError) as error: #To implement an in-line except
    print(error)
except Exception as error:   #No except is used after this.
    print(error)
finally:
    print("Hogaya khatam")  #To print any statement compulsorily, whether or not the exception occurs

