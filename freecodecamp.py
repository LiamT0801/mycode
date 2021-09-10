# # # #Expressions
# # # #Numberic expressions (/,**,%)
# # # #Types(int, string, boolean)
# # # #Python CANNOT connect int + string

# # # #type():

# # # #Type conversion:
# # # print(float(99)+100)

# # # i = 42
# # # f = float(i)
# # # print
# # # print(f)
# # # sval = '123'
# # # ival = int(sval)
# # # print(ival+1)

# # # #user input
# # # name = input("Tell me ur name:")
# # # print(f"Welcome, {name}")

# # # #converting input, input is a string -> must convert it to int
# # # #Case using a conversion
# # # floorNumEU = int(input("What floor do you want"))
# # # floorNumUS = floorNumEU + 1
# # # print(f'US floor:{floorNumUS}')

# # #Condition Execution (if statements)
# # #two-way (if...else) either 1 or 2
 
# # #multi-way
# # # if:... elif:... else

##try/except structure (concept:If code blows up, the code will keep running)
##Try: "failed" -> run Except: " "
# num = input("Get number:")
# try:
#     value = int(num)
# except:
#     value = -1
# if value > 0:
#     print("valid")
# else:
#     print("invalid")

# temp = "5 degrees"
# cel = 0 
# fahr = float(temp)
# print(fahr)

#functions def()

big = max('hello world')

print(big)


