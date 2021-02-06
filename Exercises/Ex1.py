def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def test_prime(n):
    print(str(n) + ":\n")
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, n):
            if n % x == 0:
                return False
        return True


def checkIfFibOfNisPrime():
    while True:
        # print("\nFirst 20 fibonnacci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181.\n")
        val = int(
            input("\nEnter a fibonnacci nth number of fibonnacci sequence to calclulate and then check if prime: "))
        if test_prime(fibonacci(val)):
            print("\nPrime\n")
        else:
            print("\nNot a Prime\n")
        val = int(
            input("\nEnter 0 if you want to continue to the next exercise or anything else if you want to go again: "))
        if val == 0:
            break