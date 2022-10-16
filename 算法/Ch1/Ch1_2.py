for i in range(5):
    print(' '*(4-i),chr(i+65)*(2*i+1),sep="")


for i in range(5):
   for x in range(4-i):
        print(" ",end="")
   for k in range(2*i+1):
        print(chr(i+65),end="")
   print()

