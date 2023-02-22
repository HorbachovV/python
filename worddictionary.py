def main():
    word_dictionary = {
        'Hi': 'a way of greating',
        'Eyes': 'an organ for seenig',
        'Earth': 'a planet in space'
    }
    while True:
        word = input('Enter a word: ')
        if word == '':
            break
        if word in word_dictionary:
            print(f'{word}  {word_dictionary[word]}')
main()