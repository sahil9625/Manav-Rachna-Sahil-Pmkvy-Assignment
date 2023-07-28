print("Hello World")

# hey iam sahil 
print("hey iam good boy \n gtfthf hgyjyuf gfyyur ftyty")
'''author
sahil singh chauhan
python start '''
print("hey",6,7, sep = "~" , end = "009\n")
print("sahil")

# typecasting

# a = "1"
a = 1
# b = "2"
b = 2
# print(a+b)
print(int(a)+int(b))

# matchcase
x = int(input("Enter the value of x: "))
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    case 1:
        print("case is 1")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)    

# user input       
a = input("Enter your name: ")
print("MY name is ",a)

# x = input("enter first number: ")
# y = input("enter sec number : ")
# print(x + y)

# print(int(x) + int(y))