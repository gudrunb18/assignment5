n = int(input("Enter the length of the sequence: ")) # Do not change this line

i = 4

if n == 1:
    print(n)
elif n ==2:
    print(1,2)
elif n == 3: 
    print(1,2,3)
else: 
    print(1,2,3, end=' ')

    a=1
    b=2
    c=3

    while i <= n:
        number = a + b + c
        print(number)
        a=b
        b=c
        c=number

        i= i + 1