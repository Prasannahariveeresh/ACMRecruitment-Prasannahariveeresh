## Ref: https://byjus.com/maths/how-to-find-prime-numbers

primeCnt = 1
curNumber = 3

while primeCnt < 10001:
    isPrime = True
    for i in range(3, int(curNumber**0.5) + 1, 2):
        if curNumber%i == 0:
            isPrime = False
            break

    primeCnt += 1 if isPrime else 0
    curNumber += 2 if primeCnt < 10001 else 0

print(curNumber)