#num = int(input("Enter the number of rows: "))
#for i in range(num + 1):
  #  print('*' * i)
   # i += 1
try:
    print("pattarn printing project")
    a = int(input("Enter the number that you have to print"))
    b = int(input("Enter '1'or '2' \n 1 for Increamental order pattarn or 2 for decreamental order \n Enter hare \n "))
    if b == True:
        for i in range(1,a+1):
            for j in range(1,i+1):
                print("*",end="")
            print()
    elif b==False:
        for i in range (1,a+1):
            for j in range(0,a+1-i):
                print("*",end="")
            print()
    else:
        print("You are not followed above instruction")
except Exception as e:
    print(e , " \n Some thing is wrong kaka")
