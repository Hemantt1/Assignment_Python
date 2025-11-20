a = int(input())
b = int(input())
c = int(input())

maximum = a if a > b and a > c else b if b > c else c
print(maximum)
