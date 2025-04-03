
number = int(input("Number of prime numbers : "))
print(number)

lower = 0
num = 1

print("no. of Prime numbers : ", number)

while lower < number:

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            lower += 1  # number of prime numbers found
    num += 1
