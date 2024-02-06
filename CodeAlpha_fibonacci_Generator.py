def fibonacci_Generator():
    a=0
    b=1
    n = int(input("Enter any value from you want to generate fibonacci series: "))
    print(a)
    for i in range(n):
        print(b)
        a,b=b,a+b

obj = fibonacci_Generator()


