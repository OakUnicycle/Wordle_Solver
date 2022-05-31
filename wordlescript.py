def wordcolours(correctword, guess):
    colours = ['', '', '', '', '']
    colouroutput=''
    correct = list(correctword)
    word = list(guess)
    for index, value in enumerate(word):
        if value == correct[index]:
            colours[index] = 'g'
            word[index] = '_'
            correct[index] = '_'
    for index, value in enumerate(word):
        if (value in correct) and (value != '_'):
            colours[index] = 'y'
            word[index] = '_'
            correct[correct.index(value)] = '_'
        elif not(value in correct):
            colours[index] = 'b'
    for i in colours:
        colouroutput = colouroutput + i
    return colouroutput # returns the colours of if the guess was entered and the correct word was correctword
