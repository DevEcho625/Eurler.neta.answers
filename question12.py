def factorCount(number):
    factorCount = 0
    if number <= 0:
        raise ValueError("Must be more than 0")
    for i in range(1, int(number**0.5+1)):
        if number%i == 0:
            factorCount = factorCount + 1
    return 2*factorCount

print(factorCount(4))
triangleNumbers = []
for x in range (1, 50000):
    triangleNumbers.append(x*(x+1)*0.5)
print(1)

for x in triangleNumbers:
    if factorCount(x) >= 500:
        print(x)

print(factorCount(triangleNumbers[len(triangleNumbers)-1]))
print("HI")
