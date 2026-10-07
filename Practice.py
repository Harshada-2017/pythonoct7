# sum of first 10 numbers
sum = 0
count = 0

while count < 10:
    n = int(input("Enter number: "))

    if n % 2 == 0:
        sum = sum + n
        count = count + 1

print(sum)
