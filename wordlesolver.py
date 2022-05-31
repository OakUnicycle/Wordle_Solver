#gets the words from the answers file
def getwords():
    try:
        with open("answers.txt", "r") as answers:
            words = answers.read().splitlines()
        return words
    except FileNotFoundError:
        print("file not found")

#get the wrong(black) letters from the guess and colours
def wrongLetters(result, attempt):
    wrong = []
    for ind, char in enumerate(result):
        if char == 'b':
            wrong.append([attempt[ind], ind])
    return wrong

#get the semi-correct(yellow) letters from the guess and colours
def partialLetters(result, attempt):
    partial = []
    for ind, char in enumerate(result):
        if char == 'y':
            partial.append([attempt[ind], ind])
    return partial

#get the correct(green) letters from the guess and colours
def correctLetters(result, attempt):
    correct = []
    for ind, char in enumerate(result):
        if char == 'g':
            correct.append([attempt[ind], ind])
    return correct


#check if the word is possible
def check_word(x, col, gue):
    wrong_word = False
    wrong_letters = wrongLetters(col, gue)
    partial_letters = partialLetters(col, gue)
    correct_letters = correctLetters(col, gue)
    word = [char for char in x]

    for c in correct_letters:
        if c[0] == word[c[1]]:    # if correct letter in correct place
            word[c[1]] = '_'
        else:
            wrong_word = True
            break

    if not wrong_word:
        for p in partial_letters:
            if p[0] in word:   # if yellow letter in word
                if word.index(p[0]) in ([i[1] for i in partial_letters if i[0]==p[0]]):
                    wrong_word = True
                    break
                else:
                    word[word.index(p[0])] = '_'
            else:
                wrong_word = True
                break

    if not wrong_word:
        for w in wrong_letters:
            if w[0] in word:
                wrong_word = True
                break
    return wrong_word # Returns true if it is a wrong word


#removes impossible items from the list
def removelist(currentlist, guess, colours):
    remove = []
    templist = currentlist[:]
    for index, value in enumerate(templist):
        if check_word(value, colours, guess):
            remove.append(index)

    for a in remove[::-1]:
        templist.pop(a)
    return templist


#a main function so that the code can run on its own to just eliminate words
def main():
    possible = getwords()
    running = True
    while running:
        guess = input("enter word entered:    ").lower()
        colours = input("enter colours outputted (b,y,g):    ").lower()
        possible = removelist(possible, guess, colours)
        print(possible)


if __name__ == "__main__":
    main()
