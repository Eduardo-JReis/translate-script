# import googletrans as gt
from googletrans import Translator

# print(gt.LANGUAGES)

trans = Translator()

test = True

while test:

    word = str(input('Digite a palavra: '))

    print()

    res = trans.translate(word, dest='pt')

    print(res.text)

    if word == 'esc':
        test = False
