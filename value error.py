try:
    num=int(input("Enter a number : "))
    print (num)

except ValueError as ex :
    print("exception", ex)
print ("im the last block")
