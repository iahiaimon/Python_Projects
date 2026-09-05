# a = 123
# b = str(a)
# print(type(b))

# print(b)

# word = "amaging"
# print (word[0::1])

# story = "There are nothing to see. You can just go to bed and sleep tight"
# number = 12345678911554499
# print(len(story))
# # print(number.count(5))
# print(story.count("a"))
# print(story.find("can"))


# list = [ 2, 4, 7, 1, 3, 2, 8 , 10 , "string", 6, "code", "life"]
# # l1 = list.sort()
# print(list.append(2))
# print(list)
# print(list.insert(3,8))
# print(list)
# print(list.remove(8))
# print(list)
# l1 = list.count(2)
# print(l1)


# for i in range (5):
#     print("print")
#     if i == 2 :
#         continue
#     print(i)

# user = int(input("Enter the number: "))
# for i in range(1,21):
#     print(user*i)

# l = ["iahia", "imon" , "shanto" , "ryhan" , "imam" , "safin" , "imran"]

# for name in l:
#     if name.startswith("i"):
#         iname = name
#         print(f"Hello {name}")


# num = int(input("Enter the number : " ))
# i = 0 
# sum = 0
# while i<=num : 
#     sum += i
#     i += 1
# print(sum)

# for i in range (1,11,2):

#     print('*'*i)

# number = int(input("Enter the number: "))
# for i in range (1 , number+1):
#     print(" " * (number-i)+"*"*(2*i-i))


# def factorial(n):
#     if n==0 or n == 1:
#         return 1
#     else:
#         return n*factorial(n-1)

# n = int(input("Enter the factorial number: "))
# print(f"The factorial of {n} is: {factorial(n)}")

# def big(a,b,c):
#     if a>b and a>c:
#         print("A the is greatest number")
#     elif b>c:
#         print("B is the greatest number")
#     else: 
#         print("C is ")
# a = int(input("Enter a number "))
# b = int(input("Enter a number "))
# c = int(input("Enter a number "))
# big(a,b,c)

# def farenheit(c):
#     return c*(9/5)+32
# c = int(input("Enter tha tempareture: "))
# res = farenheit(c)
# print(round(res,2))

# Sum Of N Natural number 

# def sum(n):
#     if n==1:
#         return 1
#     return sum(n-1)+n
# print(sum(5))

# def patterns(n):
#     if n==0:
#         return
#     print("*" * n)
#     patterns(n-1)

# patterns(3)


l = ["iahia" , "imon", "noyon" , "leon" , "on"]

def rem(l , word):
    n = []
    for item in l:
        if (item != word):
            n.append(item.strip(word))
    return n

print(rem(l , "on"))