try :
    num1=int(input("enter a number : "))
    num2=int(input("enter a number : "))
    result=num1/num2
    print("result is ",result)
    print("result is",result1)

except ZeroDivisionError :
    print("division by 0 is not allowed")
except ValueError :
    print("Please enter numbers only") 
except NameError as ex :
    print("the exception is", ex)
except :
    print("some error occured idk which")
finally :
    print ("i am immune to errors trying to stop me hahaha")