# function syntax
# def functionRada(a,b,c):
#     """ this function will calcalate average of three number
#     function chya khalchi first line doc string mhanun  print hote"""
#    average = (a+b+c)/2
#     return average
# v= functionRada(6,6,6)
# print(v)
#
#
# print (functionRada.__doc__)
#
#
# Try Except Exception Handling.
#
# print("Enter num1")
# num1 = input()
# print("Enter num 2")
# num2 = input()
# try:
#     print("The some of these two number is ")
#     int(num1) + int(num2)
# except Exception as e:
#     print(e)
#
# print("This line is vary important") # var kuth error aala tari khalchi line print karnyasathi try except vapartat


# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)


harry()
print(x)

# l = 10 # Global
#
# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")
#
# function1("This is me")
# # print(m)

x = 89


def harry():
    x = 20

    def rohan():
        global x
        x = 88

    # print("before calling rohan()", x)
    rohan()
    ("after calling rohan()", x)



harry()
print(x)

