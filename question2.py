 def fibonacci_sequence(number):
    if number == 1:
        return 1
    if number == 2:
        return 2
    return fibonacci_sequence(number -1) + fibonacci_sequence(number-2)

number = 1
evenFibsUnder = []
while fibonacci_sequence(number) <= 4000000:
    if fibonacci_sequence(number)%2 == 0:
        evenFibsUnder.append(fibonacci_sequence(number))
    number+=1
total = 0
for x in evenFibsUnder:
    total = total + x
print(total)
