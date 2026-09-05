def multiplecation_table(n):
    with open(f"Table/table_of_{n}" , "w")as f:
        for i in range (1,21):
            mul = n*i
            data = f.write(f"{i} X {n} = {mul}\n")
        print(f"The table of {n} is added  to the file ")

def fun(n):
    while n<21:
        multiplecation_table(n)
        n+=1
fun(1)