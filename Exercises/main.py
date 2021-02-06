# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Ex1 import checkIfFibOfNisPrime

from Ex2 import getKinoNumbersForFirstDateOfMonth
from Ex3 import getRandomTextFromFile
from Ex4 import getNumberOfSoS
from Ex5 import getOddCharactersfFromFile


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Exercise 1
    checkIfFibOfNisPrime()

    # # Exercise 2
    getKinoNumbersForFirstDateOfMonth()

    #Exercise 3
    print(getRandomTextFromFile('Fox.txt'))

    #Exercise 4
    cnt = getNumberOfSoS(int(input("Enter x >>> ")), int(input("Enter y >>> ")))
    print("SOS appears " + str(cnt) + " times")

    #Exercise 5
    print(*getOddCharactersfFromFile('Fox.txt'), sep=' ')
