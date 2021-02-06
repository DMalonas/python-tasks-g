
def getOddCharactersfFromFile(file):
    file = open(file, 'r')
    oddCharacters = []

    while 1:
        # read by character
        character = file.read(1)
        if not character:
            break
        if ord(character) % 2 != 0:
            oddCharacters.append(character)
    file.close()
    return oddCharacters