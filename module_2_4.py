from math import sqrt

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers)
primes = list()
not_primes = list()

for i in numbers:
    flag = True
    if i == 1:
        continue
    elif i == 2:
        primes.append(i)
        continue
    else:
        for j in primes:
            if i % j == 0 or sqrt(i) in primes or i / j in primes:
                flag = False
                break
            else:
                flag = True
    if flag:
         primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)








