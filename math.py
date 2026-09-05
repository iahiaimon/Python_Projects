class small_problems():
    def min_num():
        a = int(input("Enter a : "))
        b = int(input("Enter b : "))

        if a==b:
            print("Input numbers are Equal Please try new number")
            return
        if a>b:
            print("B is the minimum number")
        else:
            print("A is the minimum number")

    def sum_n():
        n = int(input("Enter the range of number : "))
        count = 1
        sum = 0
        while count<=n:
            sum +=count
            count +=1
        print("sum of numbers is " , sum)

    def prime():
        n = int(input("Enter the number: "))
        for i in range (2,n-1):
            if n%i == 0 :
                print("number is not prime")
                return
            i+=1
        else:
            print("The number is a prime number")

    def factorial():
        n = int(input("Enter the number: "))
        count = 1 
        factor = 1
        while count<=n:
            factor = factor*count
            count+=1
        print(f"The factorial of {n} = {factor}")
    
    def F(n):
        if n<5:
            return F(n+1) + F(n+2) + F(n+3)
        else:
            return n
    F(2)