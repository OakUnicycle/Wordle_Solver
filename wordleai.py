import wordlesolver
import wordlescript
import math


words = wordlesolver.getwords()
wordslen = len(words)
guess1 = True
official = input('Do you want to use the official wordle answer bank:   ').lower()
if official == 'y':
    possible = words[:2309]
    wordscores = [['soare', 5.885202744292758], ['roate', 5.884856313732008], ['raise', 5.878302956493168], ['reast', 5.867738020843561], ['raile', 5.86515382904127], ['slate', 5.855819244109513], ['salet', 5.836022782092482]]
else:
    possible = words[:]
    wordscores = [['tares', 6.244052544375447], ['lares', 6.199918742453126], ['rales', 6.1643430994542285], ['rates', 6.1462426425146015], ['teras', 6.126619177276175], ['nares', 6.116830765753897], ['soare', 6.11139539909626]]


running = True
while running:
    if not guess1:
        wordscores = []
        for index, currentword in enumerate(words):
            currentwordscores = []
            pools = []
            colourpatterns = []
            colourcounts = []
            for theword in possible:
                thecolour = wordlescript.wordcolours(theword, currentword)
                if thecolour in colourpatterns:
                    colourcounts[colourpatterns.index(thecolour)] += 1
                else:
                    colourpatterns.append(thecolour)
                    colourcounts.append(1)

            total = 0
            for i in colourcounts:
                probability = i / len(possible)
                score = probability * math.log((1 / probability), 2)
                total+=score
            if currentword in possible:
                total += 0.0001
            wordscores.append([currentword, total])
            if index % 60 == 0:
                percent = 100 * (index / wordslen)
                print(f'{percent}% done')

        print(possible)
    if guess1:
        guess1 = False
    wordscores.sort(key=itemgetter(1), reverse=True)
    print('computer suggests the words:', wordscores[:7])

    guess = input("enter word entered:    ").lower()
    colours = input("enter colours outputted (b,y,g):    ").lower()
    remove = []
    possible = wordlesolver.removelist(possible, guess, colours)

