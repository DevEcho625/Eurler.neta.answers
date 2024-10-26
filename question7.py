highest = 10001

def prime_checker(number):
    if number < 2:
        return False
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True

counter = 2  # Start from 2, the first prime
prime_count = 0

while prime_count < highest:
    if prime_checker(counter):
        prime_count += 1
        print(counter)
        if prime_count == highest:
            print(counter)
            break
    counter += 1

  
